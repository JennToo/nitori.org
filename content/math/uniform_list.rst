Problem: Finding a list subset with uniform distribution
########################################################

:date: 2020-10-16
:modified: 2020-10-18
:summary: A surprisingly difficult problem
:tags: math
:slug: uniform_list

Context
=======

Continuous integration will often produce a lot of builds for a product under
active development. If our build artifacts are large (perhaps in the GB range)
we will need to start pruning old builds.

A simple solution for pruning builds is just to discard builds older than a
certain date. However, it can sometimes be useful to preserve a few olds
builds [1]_. This can be especially useful when trying to track down an obscure bug.
If we have a few old builds around, we can more effectively bisect_ commits to
try and find the culprit.


So we might want to have an aggressive pruning policy for maybe the last two
weeks or so. But we also want to preserve 15 builds from the last year. And
ideally we'd like those 15 builds to be spaced apart in time [2]_ as far as
possible.

Since we're implementing continuous integration, our builds could happen at any
time. Thus the problem presents itself: if we have a list of all the builds in
the last year, how do we choose which builds should be pruned and which should
be kept?

Formalized Problem
==================

Given a sorted list :math:`A` of size :math:`n`, find the sorted sub-list
:math:`B` with size :math:`m` where :math:`2 < m < n` such that the items of
sub-list :math:`B` are "uniformly spaced" and :math:`A_0 = B_0,
A_{n-1}=B_{n-1}` (i.e. preserving the first and last elements of :math:`A`).

Formally, by "uniformly spaced" I mean that this metric should be minimized:

.. math::

   \sum_{i=1}^{m-2} |(B_{i+1} - B_i) - (B_i - B_{i-1})|

A few test examples:

.. math::

   \begin{aligned}
   A = [1, 2, 3]; m=2 \quad &\Rightarrow \quad B = [1, 3] \\
   A = [1, 4.5, 4.6, 5, 5.1, 5.2, 6, 9]; m=3 \quad &\Rightarrow \quad B = [1, 5, 9] \\
   A = [1, 2, 3, 4, 5, 6, 7]; m=4 \quad &\Rightarrow \quad B = [1, 3, 5, 7]
   \end{aligned}

In each of these examples, the metric given above is :math:`0`

.. _bisect: https://git-scm.com/docs/git-bisect

.. [1] Hermetically reproducible builds is another possible solution
.. [2] One could also argue that it's better to be uniformly spaced between
   build numbers, as it would preserve more builds from a period of more active
   development, making bisection more efficient
