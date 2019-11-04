Creating a Persistent SSH Tunnel as a SystemD User Service
##########################################################

:date: 2019-11-4
:summary: HTTPS is hard, but SSH is easy!
:tags: linux, ssh

Motivation
==========

I use `ownCloud <https://owncloud.org/>`_ to sync binary files between the
various computers I use. It's basically like Google Drive or OneDrive, but
hosted on your own hardware. Which is great, because the last thing I want is
for Google or Microsoft to get their hands on my meme collection!

But there's a problem with setting up ownCloud: getting HTTPS running is really
annoying. I'm sure if I spent enough time on it I could get it to work, but
that's more trouble than I'd like to deal with.

So as an alternative, I'd like to just use plain HTTP to connect to the
service. But since that would be a bad idea over the Internet, we need some
other solution to secure the connection. Enter: the SSH tunnel

SSH Tunnels
===========

I already have secure access to my server setup for SSH which only allows
key-based login. And with a simple ``ssh`` command I can use an SSH connection
to reach any other port on the server, like this::

    ssh -NTC -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 8080:localhost:8080 <my_server>

As a disclaimer, I totally snagged this command from a Google search, but I
don't remember where.

Let's go through each option in that command since we seem to be doing quite a
bit:

``-N``
  Don't execute any remote commands. We're just interested in the tunnel itself.

``-T``
  Disable PTY. We're not running any commands and we don't plan to run this
  interactively so it's not needed anyways.

``-C``
  Use compression on the link. We're transferring a lot of data over the
  Internet with this tunnel, so this seems prudent to save bandwidth.

``-o ServerAliveInterval=60``
  Send a keep-alive message every 60 seconds if no other data has been sent.
  This will help make sure any firewall sessions don't expire. You might have
  to tweak the value depending on how aggressive your firewall is.

``-o ExitOnForwardFailure=yes``
  This will cause the ``ssh`` process to die if it can't establish the
  connection. This is preferable since we're going to run this with SystemD and
  the exit will communicate to SystemD that something went wrong.

``-L 8080:localhost:8080``
  This is the option that's doing most of the work! It sets up a port-forward
  such that port 8080 on the current machine will map to port 8080 on the
  remote machine. For more details about the syntax of this option, check out
  the man page for ``ssh``.

Once the tunnel is up I just connect ownCloud to ``http://localhost:8080`` and
everything works great!

SystemD User Service
====================

Pretty much any modern Linux system is using SystemD. This has led to a great
deal of complaining.

One neat feature of SystemD is that it support defining services for an
individual user. These services can be automatically started when the user logs
in, which makes it the perfect tool to automatically start the SSH tunnel!

We just need to write a ``.service`` file and drop it in
``~/.config/systemd/user/``. Mine looks like this:

.. code-block:: ini

    [Unit]
    Description=ownCloud SSH tunnel
    After=network.target

    [Service]
    Environment="SSH_AUTH_SOCK=/run/user/1000/keyring/ssh"
    ExecStart=/usr/bin/ssh -NTC -o ServerAliveInterval=60 -o ExitO...
    RestartSec=3
    Restart=always

    [Install]
    WantedBy=default.target

I won't get into the details about what everything in this file does. But there
are a few items to take specific note of:

``Environment="SSH_AUTH_SOCK=/run/user/1000/keyring/ssh"``
  My SSH key files are generally locked with a passphrase, so this makes sure
  that the tunnel can be opened once I login and unlock the key. I'll be
  honest, I don't like this very much since it's hard-coded to UID 1000.
  There's probably a cleaner way to do it.

``WantedBy=default.target``
  This is how you make sure the service gets started up automatically when you
  login.

Now that we have a service file, we could use typical ``systemctl`` commands to
get it up and running. We just have to be sure to pass ``--user`` to make sure
it's operating on the user-specific services instead of the global ones. But
using ``systemctl`` to install the service is pretty manual, so I don't like to
use it.

Automating It
=============

There's `no place quite like home
<https://github.com/Nitori-/no-place-like-home>`_, so I maintain a set of
Ansible scripts to keep all the machines I use configured in the same way.

Here's an Ansible blob that will enable and start our new SystemD user service:

.. code-block:: yaml

    - name: Enable owncloud tunnel service
      systemd:
        state: started
        enabled: yes
        scope: user
        daemon_reload: yes
        name: owncloud-tunnel

Conclusion
==========

This method of securing access to ownCloud is pretty convenient. It lets me
just open a single hole in my home firewall for SSH, which definitely seems
more secure. And it's way easier than setting up HTTPS.

There are some downsides to this approach though. By locking the ownCloud
frontend behind SSH, I can't really connect to it on my phone unless I'm at
home. I don't use ownCloud on my phone that much anyways, so this isn't a deal
breaker for me.
