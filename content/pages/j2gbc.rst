j2gbc
#####

:slug: j2gbc

j2gbc is a Game Boy and Game Boy Color emulator.

My motivation for writing it was twofold.

First, I wanted to try out Rust on a full-sized project. I had used it on a few
toy projects before but I wanted to try something of a larger scope to see how
the language plays out at a larger scale (spoiler alert: Rust is pretty good at
this!).

My other motivation was to find a side project that I would actually make
decent progress on. And as it turns out, writing an emulator for an old game
system like the Game Boy is perfect for this! There's always something I can
tinker on, even for 15 minutes, and see real forward progress on the overall
project. This helps maintain momentum, even on the "hard parts" of the project.

The Game Boy (and really most game consoles from before the N64 / PS1 period)
are fun systems to work with, since the mental model for the entire system can
fit into one developer's head. If you want to, you can know in exact detail how
pretty much any part of the system functions! Which is a far cry from today's
computing platforms.

Screenshots
===========

These screenshots were produced with legally obtained ROMs! I actually have the
cartridges for them, and a little $30 peripheral that can dump those cartridges
into usable ROMs.

In my not-legally-trained opinion, reproducing these screenshots to demonstrate
the functionality of this emulator falls under fair use. The presence of these
screenshots does not represent any endorsement or even permission from the
respective copyright holders.

TODO: Add some screenshots

Functionality Overview
======================

Graphics:
 - Things mostly work here, both DMG and CGB. I stumble onto visual glitches
   every once in a while but they're usually easy to fix.
 - The biggest missing piece for graphics is that the timing of certain "video
   states" isn't emulated cycle-accurately. Because this timing can vary with
   the number of sprites visible on a specific scanline, it can be a little
   tough to emulate this properly.

Audio:
 - This is mostly functional, but it still has a lot of glitches.
 - I think I need to fundamentally re-think the audio stack to fix several of
   the timing issues.
 - I've never worked with computer audio before this project so this part was
   definitely a big learning experience!

System (CPU and peripherals):
 - CPU instructions are all implemented and function correctly. There's a great
   set of test ROMs developed by the GB community that help verify this.
 - Cycle accuracy is lacking on a variety of things. E.g. DMAs are all
   essentially instant right now, which is definitely inaccurate.
 - The link cable and IR system (CGB only) are not implemented, but this would
   be really cool for the future! I'd like to get it running over the internet
   so you could play multiplayer games remotely.

Debugger:
 - This is very much a work-in-progress. Right now you can get disassembly
   around the current PC, and do single steps. Breakpoints are supported by the
   CPU core but I need to hook them back up to the GUI.
 - There is a built-in MMU-like process in the CPU core. This will trigger a
   breakpoint when a ROM does something fishy (like e.g. jumping into the ROM
   header, or reading from a memory-mapped register that is write-only).
   There's a table with exceptions for known bugs in ROMs (e.g. Tetris does a
   lot of bad things).
 - That MMU protection was very useful early on when diagnosing CPU bugs that
   would cause the program execution to spiral out of control. It would also be
   useful for developing new ROMs.

Lessons Learned
===============

Having a project with quick positive feedback makes it much more appealing to
work on that project

Write real automated tests, even when you're just doing something for fun! This
was honestly the biggest mistake I made in this project. I was essentially
manually testing things while I was writing the original core system. Which
means I've also seen all the possible horribly corrupted variations of the
intro to Link's Awakening DX 😂 But now I have a pretty big backlog of
technical debt for the project.
