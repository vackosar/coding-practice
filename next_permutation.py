from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        for current_pos in range(len(nums) - 1, 0, -1):
            # print(current_pos)
            current_num = nums[current_pos]
            comparison_num = nums[current_pos - 1]
            if comparison_num < current_num:
                for j in range(len(nums) - 1, current_pos - 1, -1):
                    if nums[j] > comparison_num:
                        nums[current_pos - 1] = nums[j]
                        nums[j] = comparison_num
                        nums[current_pos:] = reversed(nums[current_pos:])
                        print(nums)
                        return nums

        # print('finish')
        nums.sort()
        return nums


assert Solution().nextPermutation([1, 2, 3]) == [1, 3, 2]
assert Solution().nextPermutation([1, 3, 2]) == [2, 1, 3]
