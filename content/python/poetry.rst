I ❤️ poetry
###########

:date: 2019-9-30
:summary: And I don't mean the kind from English class
:tags: python, poetry

poetry is a really cool Python development environment manager, and I hope I
can convince you it's cool enough for your next project. But to understand why
I like it so much it helps to have...

A bit of motivation
===================

Reproducing a build
-------------------

Imagine you're pulling down an open-source Python repository that you want to
play with. How will you setup the development environment? The process
will often take one of these forms:

- If there is a ``Makefile`` for managing the environment, use it
- If there is a ``requirements.txt`` (or similar) file, create a new
  ``virtualenv`` and ``pip install -r`` the requirements. Let's hope the
  compatible versions are well specified.
- Maybe the requirements are just in ``setup.py``, and we can install those in
  a ``virtualenv``. Who knows how we get the test dependencies.

So somehow you've managed to setup an environment with the dependent packages.
Feeling accomplished you run the tests, and watch as they explode in a
cacophony of failures.

It turns out that, compared to the last CI run for the package, you have a
slightly different version of some deep transitive dependency. And that change
breaks everything.

If you work with enough Python packages this story is all too familiar. 🙄

What is all this junk?
----------------------

Look at your average Python package repo and what kinds of files do you see?
There's the source code and tests, sure. But you've also got the likes of:

- ``setup.py`` for making the package installable
- ``MANIFEST.in`` for including extra files in the package
- ``requirements.txt``, ``test-requirements.txt``, etc. for specifying
  dependencies

Maintaining these files is annoying. They each have their own syntax and
quirks, and they pollute the repository with files that aren't really
"essential" to the package.

poetry to the rescue!
=====================

poetry tries to address both of the problems I've mentioned above (and a few
others). There are two core files present in any poetry-based Python project:

- ``pyproject.toml``, which contains most of the information about a package
  such as its name, version, description, and dependencies.
- ``poetry.lock``, which contains specific versions of the dependencies
  (transitively) used when running tests and other commands.

Here's an example ``pyproject.toml`` file for a simple Python package:

.. code-block:: toml

   [tool.poetry]
   name = "my_totally_cool_project"
   version = "0.1.0"
   description = "It does cool stuff, trust me"
   authors = ["Jennifer Wilcox <jennifer@nitori.org>"]

   [tool.poetry.dependencies]
   python = "^3.6"
   # It's a web app
   flask = "^1.1"

   [tool.poetry.dev-dependencies]
   pytest = "^4.2"
   pylama = "^7.6"
   pylint = "^2.2"
   pytest-cov = "^2.6"
   black = "18.9b0"
   sphinx = "^2.0"

   [build-system]
   requires = ["poetry>=0.12"]
   build-backend = "poetry.masonry.api"

This file alone replaces ``setup.py``, ``MANIFEST.in``, ``requirements.txt``,
``test-requirements.txt`` and more!

We've also specified our package's dependencies and dev-dependencies using the
common semver specifiers. Whenever we run ``poetry update`` it will take these
dependencies and attempt to resolve a set of packages that satisfy them. This
process also back-tracks when needed (unlike regular ``pip install``).

Once a set of packages satisfying the dependencies has been found, poetry will
generate a ``poetry.lock`` file listing all of the required packages. This
ensures that dependencies (even transitive dependencies) are only changes when
specifically requested, yielding greatly improved build reproducibility.

What tool doesn't have shortcomings?
====================================

There are a few problems I run into with poetry from time to time.

The one I hit the most frequently is the lack of ability to specify tasks. For
example, defining ``poetry test`` to be ``pytest -vvl tests/``. I really,
truly, do not want to write a ``Makefile``, but this limitation often leads you
down that road.

This issue will likely be solvable once poetry `adds support for plugins
<https://github.com/sdispater/poetry/issues/693>`_, as task running has been
cited as a specific non-goal for poetry itself. It should be pretty trivial for
a plugin to add such functionality.

The other big issue that I hit very frequently isn't actually a problem with
poetry at all!

When you start adding dependencies from the wide world of Python
packages, you will come to find many packages that don't specify their
dependencies very well. Since poetry is significantly stricter in how it
evaluates dependencies (compared to pip), this can often lead to you having to
add more dependencies to your top-level ``pyproject.toml``. This problem
becomes especially common when you try to support older versions of Python
(e.g. 2.7 and 3.4 in 2019).

I'm sold!
=========

You can get started with poetry by `following the documentation on their
website <https://poetry.eustace.io/>`_.
