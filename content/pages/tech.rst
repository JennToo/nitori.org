My Technology Stacks
====================

These are the tools and programs I use for various things in my life.

.. contents::
   :backlinks: none
   :local:

Programming
-----------

You can find a lot of the tools I use for programming via my repo
`JennToo/no-place-like-home <https://github.com/JennToo/no-place-like-home>`_.

- I use **Ansible** to automatically provision my own development environment, as
  well as managing servers at home and at work. It's a very useful tool for
  ensuring a consistent state across multiple machines. It also means I can
  very quickly provision a new development environment.
- My preferred text editor is **Neovim**. It's easy to use, even over SSH.

  - And Neovim is way faster than **Emacs**. I used Emacs for about 12 years, but
    eventually it got too slow and was really making my development time
    inefficient. I do miss it sometimes, especially the Lisp elements.
  - Sometimes I will use **VS Code**, but I find it usually wants way too much
    RAM and CPU for what it's doing. And I also prefer entirely keyboard driven
    programs while programming.
- I'm proficient in a number of programming languages, but there are two that I
  reach for the most often.

  - I use **Python** by default. Most of my work doesn't require high runtime
    efficiency. Since I'm usually developing tools and CI infrastructure, the
    ability to glue disparate systems together quickly is my main priority. And
    Python is great for that. 💖🐍
  - When I need resource efficiency, I'll use **Rust**. It works well on
    embedded targets and for systems that need better performance than what
    Python can offer. I wrote `my Game Boy emulator <{filename}j2gbc.rst>`_ in
    Rust.
  - I'm also proficient with these languages, but they're not my first choices
    for new projects:

    - **C++** is fine, but not something I'll choose for a new project. The
      language is a bit of a mess, with so many wrong ways to do something. The
      tooling is also generally bad, except GDB which is great!
    - I admire **C** for its simplicity, but I wouldn't use it on anything
      bigger than a toy project if I could help it.
    - **Groovy** is not a good language at all. But since I write a lot of
      Jenkins CI pipelines at work, that involves writing a lot of Groovy 😭
    - Various **Lisps** are cool! Being `homoiconic
      <https://en.wikipedia.org/wiki/Homoiconicity>`_ is neat, especially when
      combined with macros. I also think the model of "live" programming is
      interesting, though I never really wrapped my head around it.

- For static website development I use **Pelican**. It's a `Python based site
  generator <https://getpelican.com/>`_. It turns Jinja templates and
  Markdown / reStructuredText files and turns them into webpages.

  - This website is made in Pelican!
  - I also use Pelican for maintaining `the website for our support group
    <https://altgo.us>`_.
  - I'm a big fan of static websites with no backends, and very little
    Javascript. I think most content on the web is served just fine by static
    text on a page, laid out with some simple CSS.
- I'm also a fan of `poetry for Python dependency management
  <{filename}poetry.rst>`_! Luckily, in the intervening time since I wrote that
  blogpost the wider Python ecosystem really seemed to adopt poetry quite
  heavily.

Home Services
-------------

I don't like cloud-based and subscription-based online services. Where those
things can be avoided, I will do so. To that end I host a lot of services just
at my house on a server, which itself is just an old repurposed desktop
computer.

The files configuring most of my services can be found in my `home-services
repository <https://github.com/JennToo/home-services>`_

- I use **Jellyfin** for hosting music and video content that I rip from disks
  (physical-media4life!). It has an interface very similar to video streaming
  services.

  - For mobile access to music, I use **Finamp** to connect back to Jellyfin.
    Its interface works very well on a phone, and looks more like a standard
    music streaming system.
- For basic home automation I use **Home Assistant**. I don't have many IoT
  devices, and to the capacity that I can I try and keep all of their network
  traffic within my own network. I have a few smart switches that I use to
  control fans and 3d printers, and that's about it. Home Assistant works great
  for that. There's a lot of fancy things that it can do too that I've never
  really explored. Maybe someday!

  - I mainly use this to control the fan pointed at my bed while I sleep. At
    night I can get too warm, so I like the fan on. But by the time I wake up I
    don't want to get out of bed since it's too cold! 🥶 But with a smart plug,
    I can use my phone to turn the fan off. Otherwise I'll stay in the warm and
    cozy bed too long.
- **Dokuwiki** is a very simple wiki system where I keep my notes. It's a
  little janky, but it works well enough.
- I follow RSS feeds using **FreshRSS**. It works well enough. Not fancy at
  all, just gets the job done.

  - I think when Google killed off Google Reader that's when my disdain for
    cloud hosted services really began 😡
- **nginx** combined with some DNS records makes it easy to access all the
  internal services by name. Instead of trying to remember port numbers for
  everything.
- All of the services I mentioned above are launched with **Docker**. Because
  nobody has time to be trying to figure out how to install all the crazy
  dependencies each of these services have 😂
- For storage, I have a triplet of hard drives configured with **ZFS**. I like
  ZFS a lot! In particular I like that it does frequent validation of the
  stored data. It also makes backups to an external drive very easy.
- I don't trust most of these services being exposed directly to the Internet,
  so when I need to access things remotely I use **Wireguard** for VPN. It
  works well once you have it setup. It's way easier to setup than OpenVPN.

*The Cloud is just someone else's computer.*
