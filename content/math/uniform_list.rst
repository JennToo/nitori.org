Problem: Finding a list subset with uniform distribution
########################################################

:date: 2020-10-16
:summary: A surprisingly difficult problem
:tags: math

Given a sorted list :math:`A` of size :math:`n`, find the sorted sub-list :math:`B` with size :math:`m` where :math:`2 < m < n` such that the items of sub-list :math:`B` are "uniformly spaced".

Formally, by "uniformly spaced" I mean that this metric should be minimized:

.. math::

   \sum_{i=1}^{m-1} |(B_{i+1} - B_i) - (B_i - B_{i-1})|

A few test examples:

.. math::

   \begin{aligned}
   A = [1, 2, 3]; m=2 \quad &\Rightarrow \quad B = [1, 3] \\
   A = [1, 4.5, 4.6, 5, 5.1, 5.2, 6, 9]; m=3 \quad &\Rightarrow \quad B = [1, 5, 9] \\
   A = [1, 2, 3, 4, 5, 6, 7]; m=4 \quad &\Rightarrow \quad B = [1, 3, 5, 7]
   \end{aligned}

In each of these examples, the metric given above is :math:`0`
