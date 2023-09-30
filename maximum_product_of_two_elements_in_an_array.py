import heapq
from typing import List

# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        You are given an array of integers from 1 to 10^3.
        Choose 2 different indicies i and j such that you get largest product of `(nums[i] -1) * (nums[j] -1)`.

        Examples:

        >>> Solution().maxProduct([1, 1])
        0

        >>> Solution().maxProduct([1, 2])
        0

        >>> Solution().maxProduct([2, 2])
        1

        >>> Solution().maxProduct([3,4,5,2])
        12

        >>> Solution().maxProduct([1,5,4,5])
        16

        Simplest solution is to bruteforce find maximum with collections combinations function.
        This would have N**2 time complexity.

        The second best is to search for a maximum twice, because the numbers are all positive

        The best is to use heapq and nlargest with O(N) time and O(1) space complexity.

        """

        largest = heapq.nlargest(2, nums)
        return (largest[0] - 1) * (largest[1] - 1)
