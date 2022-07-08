from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        """
        Given int list nums and an int k. Append k unique positive ints not in nums such that sum is minimal.
        Return sum of the k ints appended.

        Minimum complexity is N, since we need to read the nums as they are not sorted.
        Solution will be iterating over non existing ints in the nums from the smallest.
        Easiest is probably to sort a then iterate with skipping.
        This implies N Log N complexity.

        """

        nums.sort()
        i = 0
        count = 0
        k_attempt = 1
        k_sum = 0

        while count < k:
            if i < len(nums):
                n = nums[i]

            else:
                n = -1

            if n != -1 and k_attempt <= n and n - k_attempt < k - count:
                k_until = n - 1
                count_add = k_until - k_attempt + 1
                k_sum += (k_attempt + k_until) * count_add // 2
                k_attempt = n + 1
                while i < len(nums) and nums[i] == n:
                    i += 1

                count += count_add

            else:
                k_until = k_attempt + k - count - 1
                count_add = k_until - k_attempt + 1
                k_sum += (k_attempt + k_until) * count_add // 2
                count += count_add
                assert count == k
                return k_sum

        raise ValueError()


assert Solution().minimalKSum(
    [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84],
    35) == 794
