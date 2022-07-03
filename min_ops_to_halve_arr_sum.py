import heapq
from typing import List


class Solution:

    def halveArray(self, nums: List[int]) -> int:
        """
        List of positive ints. Reduce the sum of nums to at least half by halving selected nums. Find the minimum count of these halving needed.

        Cannot reduce more in one step than halving the biggest number.
        After each halving the biggest number changes.
        Need to keep sort and quick removal and insert.
        This sounds like heap is optimal here.


        # Computational (Time) Complexity

        Complexity cannot be faster than N. Because I need a sum at the beginning.
        If iterated sorting of complexity N * Log N is used, then total complexity is N**2 Log N.
        If heap is used, then complexity of insert is C or worst Log N, so total complexity is N Log N.


        # Memory (Space) Complexity
        Memory space needed is constant.

        """
        original_sum = sum(nums)
        nums = [float(-n) for n in nums]
        heapq.heapify(nums)

        if len(nums) == 0:
            return 0

        current_sum = original_sum
        n_operations = 0
        while current_sum * 2 > original_sum:
            neg_biggest = heapq.heappop(nums)
            current_sum -= -neg_biggest /2
            heapq.heappush(nums, neg_biggest / 2)
            n_operations += 1

        return n_operations


assert Solution().halveArray([6, 58, 10, 84, 35, 8, 22, 64, 1, 78, 86, 71, 77]) == 9
