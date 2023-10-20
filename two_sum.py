from bisect import bisect_left
from typing import List, Tuple


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i

    return None


class Solution:
    def findPair(self, nums: List[int], target: int) -> Tuple[int, int]:
        """
        Given list of numbers. Find one pair of numbers from the list that gives target sum.
        Each number can be used only once.
        Output order does not matter.
        Return an empty tuple if solution does not exist.


        >>> Solution().findPair([3, 5, 7], 10)
        (3, 7)

        >>> Solution().findPair([1, 1, 7, 2, 12], 2)
        (1, 1)

        >>> Solution().findPair([-1, -3, 7, 2, 12], -4)
        (-3, -1)

        >>> Solution().findPair([-1, 12], -2)
        ()

        >>> Solution().findPair([], 5)
        ()


        Brute force is O(N * (N-1)) with space O(1).
        Faster is to sort and then use halving to find candidate for missing sum with time O(N * Log N) but space also O(N), unless you can sort in place.

        """

        nums = sorted(nums)
        for i, n in enumerate(nums):
            n: int

            c: int = target - n
            vi = index(nums[i + 1:], c)
            if vi is not None:
                return n, c

        return tuple()