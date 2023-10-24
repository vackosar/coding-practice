import collections
from typing import *


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        # Problem Description

        Given an array of integers `nums` and an integer `k`, return the number of unique pairs in the array such that their absolute difference equals to `k`.

        # Examples Including Edge Cases

        >>> Solution().findPairs([1,2,3,4,5], 1)
        4

        >>> Solution().findPairs([3,1,4,1,5], 2)
        2

        >>> Solution().findPairs([1,2,4,4,3,3,0,9,2,3], 3)
        2

        >>> Solution().findPairs([-1,-2,-3], 1)
        2

        >>> Solution().findPairs([1,1,1,1,1], 0)
        1

        # Reasoning about Solution Approaches To Find The Best One

        The naive approach is to check all pairs, which would be O(N^2).
        The better approach is to sort the list first and then check each pair of numbers with a difference `k`. This would be O(N Log N + N).
        The best approach is to use a hashtable to store the count of each number, and then for each number in the hashtable check if it exists `num + k`. This would be O(N).

        # The Solution Implementation:
        """

        if k > 0:
            # The common case.
            nums = set(nums)
            return sum(1 for n in nums if n - k in nums)

        elif k < 0:
            # Remember the absolute value has to be larger than zero.
            return 0

        else:
            # We have to have 2 same pair.
            count = collections.Counter(nums)
            return sum(v > 1 for v in count.values())


