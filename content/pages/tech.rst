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
    Python is great for that.
  - When I need resource efficiency, I'll use **Rust**. It works well on
    embedded targets and for systems that need better performance than what
    Python can offer. I wrote `my Game Boy emulator <{filename}j2gbc.rst>`_ in
    Rust.
