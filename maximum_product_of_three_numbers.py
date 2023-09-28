import heapq
from typing import List

## Follow me for more software and machine learning at https://vaclavkosar.com/

"""
Before finding this solution, I was solving this with pure Python.
But below is inspired by a solution using Python library.
There is also a edge-case trap, that is easily missed that lead to a incorrect solution. 
"""

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Given `nums` find a subset with maximum product, and return it.

        >>> Solution().maximumProduct([1,2,3,4])
        24

        >>> Solution().maximumProduct([1,2,3])
        6

        >>> Solution().maximumProduct([-1,-2,-3])
        -6

        The simplest is to sort the array with quick sort and take top 3.
        Quick sort is time O(N log N), and space O(N).

        ```
        top_3.append(n)
        top_3 = list(sorted(top_3, reverse=True))[:3]
        ```

        The fastest would be to keep only the top 3. That would give O(N), O(1).
        But we can't do that in slow Python, better call a fast library `heapq.nlargest`.
        The nlargest documentation: https://github.com/python/cpython/blob/main/Lib/heapq.py#L397

        An edge case is presence 2 large negative numbers and one large positive.
        Imagine these 2 cancel their negativity and together with the positive form the 3 largest.

        >>> Solution().maximumProduct([1,2,-3,-4])
        24

        """

        top3_positive = heapq.nlargest(3, nums)
        top2_negative = heapq.nsmallest(2, nums)

        return max(top2_negative[0] * top2_negative[1] * top3_positive[0],
                   top3_positive[0] * top3_positive[1] * top3_positive[2])
