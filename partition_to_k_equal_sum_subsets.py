from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

        Given integer array nums and a and integer k, return true if you can divide into k non-empty same sum subsets.



        # Brute force
        Just try all splits into the k-subsets. Complexity O(k * 2**n)


        # Backtracking
        Inspired by [this solution](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/146579/Easy-python-28-ms-beats-99.5).
        
        """

        # It is the best to iterate from the biggest numbers,
        # because those cut off bad solutions close to the root of the decision search.
        # We save lots of time not repeating not trying the bad solutions again as if they are close to leaves.
        nums.sort(reverse=True)
        total_sum = sum(nums)

        # Can we even do this? Checking the reminder.
        if total_sum % k > 0:
            return False

        target_sum = total_sum // k
        sums = [0] * k
        last_index = len(nums) - 1

        def recurse(index):
            # Take number we are working with now.
            num = nums[index]
            # try to place the number into all bucket
            for bucket_i in range(k):
                # Skip already filled buckets
                if sums[bucket_i] < target_sum:
                    # try to put into bucket_i
                    sums[bucket_i] += num
                    if sums[bucket_i] <= target_sum:
                        # If fitting the last stone, we know from the reminder check, that we are done.
                        if index == last_index:
                            return True

                        # The number fits here, let's try to work with that and recurse with next index.
                        if recurse(index + 1):
                            return True

                    sums[bucket_i] -= num
                    # If we worked with empty bucket all other further buckets are empty.
                    # If the number cannot be placed into this empty bucket, it cannot be placed into others either.
                    if sums[bucket_i] == 0:
                        return False

            return False

        return recurse(0)


assert Solution().canPartitionKSubsets([1, 1, 1, 1, 2, 2, 2, 2], 4) == True
assert Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) == True
assert Solution().canPartitionKSubsets(nums=[1, 2, 3, 4], k=3) == False



"""
        # Backtracking Recursion on Each Subset Solution
        
        Keeping track of the remaining integers, filling the sets one be one.
        Backtracking, if I cannot combine the number the filled sets.
        When switching to next set I check if the remainder is divisible to the right number.
        
        Too slow.
        
        
        nums.sort(reverse=True)
        total_sum = sum(nums)
        if total_sum % k > 0:
            return False

        set_sum = total_sum // k

        def find_ints(c_sum, c_nums, f_nums, r_sum):
            for n in f_nums.copy():
                if c_sum + n == r_sum:
                    c_nums.append(n)
                    f_nums.remove(n)
                    return c_nums, f_nums

                elif c_sum + n < r_sum:
                    # don't have to copy if I would clean up
                    nf_nums = f_nums.copy(); nf_nums.remove(n)
                    # f_nums.remove(n)
                    # nc_nums = c_nums.copy()
                    c_nums.append(n)
                    result = find_ints(c_sum + n, c_nums, nf_nums, r_sum)
                    if result:
                        return result

                    else:
                        # restore state
                        # f_nums.append(n)
                        c_nums.remove(n)

                elif c_sum + n > r_sum:
                    continue

            return None

        def recurse(r_nums, r_k, r_sum):
            # find ints to sum up to the r_sum, if cannot return False, if can, do the same without those
            # maybe don't have to copy either.
            f_nums = r_nums.copy()
            c_nums = []
            result = find_ints(0, c_nums, f_nums, r_sum)
            if result is None:
                return False

            else:
                c_nums, f_nums = result
                if r_k == 1:
                    return True

                else:
                    return recurse(f_nums, r_k - 1, r_sum)

        return recurse(nums, k, set_sum)
"""
