from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/max-consecutive-ones-iii/
        
        Input is a binary array of numbers and number flip-able 0.
        Return maximum number of consecutive 1s provided you can flip k-0s.

        Quadratic complexity via going from the left and filling k-zeros in interrupted sequence with 1s.
        For each position try how far I can get. Then go back. N * (k to N) complexity.

        Instead, could use start and end pointer to define k-zero sliding window.
        And move the start and end such that I keep K-zeros in.
        Then distance between stand and end is the 1-size.
        The advantage of pointers is that I just do the operation of searching next zero twice.
        So the complexity is additive here.
        I do not have to repeat the operations, so I keep the complexity linear.
        """

        if len(nums) == 0:
            return 0

        # initialize the window, such that both point to a position with zero.
        start = 0  # points to an index after the last zero 0 that won't be flipped
        end = -1  # points to the first 0 that won't be flipped

        remaining_zeros = k
        for i in range(start, len(nums)):
            if nums[i] == 0:
                remaining_zeros -= 1
                if remaining_zeros < 0:
                    end = i
                    break

        if end == -1:
            # we reached the end without using up the flipping zeros
            return len(nums) - start

        max_len = end - start
        # print(f'{nums}')
        # print(f'{nums[start:end]}')
        # print('---')
        while True:
            # print(f'{nums[start:end]}')
            for i in range(start, len(nums)):
                if nums[i] == 0:
                    if i == len(nums) - 1:
                        return max_len

                    start = i + 1
                    break

            for i in range(end + 1, len(nums) + 1):
                if i == len(nums):
                    return max(max_len, i - start)

                if nums[i] == 0:
                    end = i
                    break

            max_len = max(max_len, end - start)


assert Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10

assert Solution().longestOnes(
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    2
) == 6

