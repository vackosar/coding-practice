from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """

        https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

        Input is array of distinct integers.
        Return rearranged array such that every element is not average of its 2 neighbors.

        The integer is an average, if both neighbors have the same distance.
        We can use sort, but quick sort average complexity is O(N logN) time, O(log n) space.


        # Swapping Sorted If Problem Found
        Sort, then iterate and if the problem found, swap the right neighbor with the next a problem.
        This will preserve the left side but break the pattern on the right.
        The last I can swap with the first, and that won't break the rule if len > 3,
        because the introduced numbers will be more than 1 distance from both.

        [1,2,3,4,5] -> [1,2,4,3,5]
        [6,2,0,9,7] -> [0,2,6,7,9] -> [9,2,6,7,0]

        See the code below.


        # Swapping into Smaller or Bigger than Neighbors

        Sort, then iterate with step 2 and swap middle and left such that the middle number is smaller or bigger than both.
        [1,2,3,4,5] -> [2,1,4,3,5]

        Solution from: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/discuss/1403927/JavaC%2B%2BPython-Easy-Solution


        # Smaller than Median on Odd and Bigger on Even in Linear Time

        To be faster than sort. We need linear time to find median.
        There is a recursive algo, which reduces the

        """


        # This is implementation of "Swapping Sorted If Problem Found" in above.

        if len(nums) <= 2:
            return nums

        nums.sort()
        for i in range(1, len(nums) - 1):
            next_num = nums[i + 1]
            if (nums[i - 1] + next_num) == 2 * nums[i]:
                if len(nums) == 3:
                    nums[2] = nums[i]
                    nums[1] = next_num
                    return nums

                next_next_i = (i + 2) % len(nums)
                next_next_num = nums[next_next_i]
                nums[next_next_i] = next_num
                nums[i + 1] = next_next_num

        return nums
