from typing import List


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # split into halves until finding element on the left corner and the right corner
        # first I will just look for the left interval
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]

            else:
                return [-1, -1]

        def find(split_left_condition, nums, target):
            right_i = len(nums) - 1
            left_i = 0
            while right_i - left_i > 1:
                split_i = left_i + (right_i - left_i) // 2
                if split_left_condition(nums, split_i, target):
                    left_i = left_i
                    right_i = split_i

                else:
                    left_i = split_i
                    right_i = right_i

            return left_i, right_i

        # left most target
        if nums[0] == target:
            result_li = 0

        else:
            left_i, right_i = find(lambda nums, split_i, target: nums[split_i] >= target, nums, target)
            if nums[right_i] == target:
                result_li = right_i

            else:
                return [-1, -1]

        if nums[-1] == target:
            result_ri = len(nums) - 1

        else:
            left_i, right_i = find(lambda nums, split_i, target: nums[split_i] > target, nums, target)
            if nums[left_i] == target:
                result_ri = left_i

            else:
                return [-1, -1]

        return [result_li, result_ri]


assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
