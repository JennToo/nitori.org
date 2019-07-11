I ❤️ poetry
###########

:date: 2019-7-10
:summary: And I don't mean the kind from English class
:tags: python, poetry

``poetry`` is a really cool Python development environment manager, and I hope
I can convince you it's cool enough for your next project. But to understand
why I like it so much it helps to have...

A bit of motivation
===================

Reproducing a build
-------------------

Imagine you're pulling down an open-source Python repository that you want to
play with. How will you setup the development environment? The process
will often take one of these forms:

 - If there is a ``Makefile`` for managing the environment, use it
 - If there is a ``requirements.txt`` (or similar) file, create a new ``virtualenv``
   and ``pip install -r`` the requirements. Let's hope the compatible versions
   are well specified.
 - Maybe the requirements are just in ``setup.py``, and we can install those in
   a ``virtualenv``. Who knows how we get the test dependencies.

So somehow you've managed to setup an environment with the dependent packages.
Feeling accomplished you run the tests, and watch as they explode in a
cacophany of failures.

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
quirks, and they polute the repository with files that aren't really
"essential" to the package.

poetry to the rescue!
=====================

TODO

What tool doesn't have shortcomings?
====================================

TODO
