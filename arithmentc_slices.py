from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        arr: List[int] is arithmettic if len(arr) >= 3 and if exists C such that arr[i] - arr[i+1] = C.
        Given array nums, return number of arithemtic continuous subarrays of nums.

        This is at least linear, bc have to go through the list. But constant in memory.
        Keep start  index, continue until the diff changes.
        """

        if len(nums) <= 2:
            return 0

        found = 0
        diff = nums[1] - nums[0]
        start = 0
        for i in range(2, len(nums)):
            current_diff = nums[i] - nums[i - 1]

            if current_diff == diff:
                n = i - start + 1
                if n >= 3:
                    found += n - 2
                    print(nums[start:i + 1])

            else:
                diff = current_diff
                start = i - 1

        return found


assert Solution().numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]) == 2
