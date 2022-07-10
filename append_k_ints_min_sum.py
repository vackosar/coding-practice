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
        
        
        # Iterating over K is very slow as K can be very large in this problem.
        # We don't need to do this, since the sums can be calculated fast.

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


        # Instead we can binary search for the K using the summation formula for K.
        # Thanks to boundaries the search is Log N.
        # This is still too complicated. Notice that we are always thinking only about the nums.

        nums = list(set(nums))
        nums.sort()
        k_right = k + len(nums)
        k_left = k

        while True:
            k_max = (k_left + k_right) // 2
            n_arr_based_on_k = [n for n in nums if n <= k_max]
            if k_max - len(n_arr_based_on_k) < k:
                k_left = k_max + 1

            elif k_max - len(n_arr_based_on_k) > k:
                k_right = k_max - 1

            if k_max - len(n_arr_based_on_k) == k:
                return k_max * (k_max + 1) // 2 - sum(n_arr_based_on_k)

        # So instead, just find the first of the nums `i` that we will not be skipping during the summation.
        """

        nums = list(set(nums))
        nums.sort()

        if nums[len(nums) - 1] <= k + len(nums):
            j = k + len(nums)
            res = (j + 1) * j // 2 - sum(nums)
            return res

        i_left = 0
        i_right = len(nums) - 1
        while i_left < i_right:
            i = (i_left + i_right) // 2
            k_guess = nums[i] - (i + 1)

            if k_guess <= k:
                i_left = i + 1

            else:
                i_right = i

        j = i_left + k
        res = (j + 1) * j // 2 - sum(nums[:i_left])
        return res


assert Solution().minimalKSum(
    [1, 4, 25, 10, 25]
    , 2
) == 5


assert Solution().minimalKSum(
[5,6],
6
) == 25

assert Solution().minimalKSum(
    [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84],
    35
) == 794

assert Solution().minimalKSum(
    [20, 83, 66, 95, 76, 36, 44, 40, 21, 93, 83, 51, 8, 26, 96, 42, 4, 64, 63, 72, 18, 80, 25, 27, 22, 68, 27, 24, 83,
     57, 4, 54, 35, 38, 52, 63, 25, 66, 32, 75, 22, 97, 54, 83, 40, 46, 9, 84, 76, 46, 56, 44, 75, 21, 4, 28, 67, 79,
     48, 52, 83, 82, 73, 99, 75, 10, 51, 92, 49, 79, 58, 54, 33, 19, 96, 11, 27, 48, 42, 6, 27, 96, 7, 26, 26, 50, 97,
     83, 14],
    24
) == 710
