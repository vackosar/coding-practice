from typing import List, Callable

# Simple With Unit Tests for a Quick Understanding
## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        You are given an array `nums` sorted in non-decreasing order.
        Return the maximum between the number of positive integers and th number of negative integers.
        In other words, if number of positives is pod and negatives is neg then return maximum(pos, neg).
        Zero is not positive and not negative.


        # Examples

        >>> Solution().maximumCount([-2, -1, -1, 1, 2, 3])
        3

        >>> Solution().maximumCount([-2, -1, 1, 2, 3])
        3

        >>> Solution().maximumCount([-2, -1, -1, 1, 2])
        3

        >>> Solution().maximumCount([-2, -1, 1, 2])
        2

        >>> Solution().maximumCount([-2])
        1

        >>> Solution().maximumCount([1, 2, 20, 80])
        4

        >>> Solution().maximumCount([0])
        0

        >>> Solution().maximumCount([-1])
        1

        >>> Solution().maximumCount([0, 0, 0, 1])
        1


        # Approaches
        The simplest is just to go and count positives and negatives, then calculate the max.

        Since we have sorted array, and we need to have just counts, which is split the array, we can do this in O(Log N).
        So just split the array. So we will use the "conditions" of sort, max.
        The split will use one divider, that will stay positive integer and will move in halves.
        But once we have the divider, it could be also full of zeros.
        The best is to treat zero as positive, but then substract it.
        But that also means to find the divide twice!


        # Code

        Common problems are off-by-one errors:
        - Function is_on_right must return correct value, when there is no value on the right. Return max position + 1.
        - Pay attention to converting position indexes to counts. Count is length but position is length minus one. They differ by one.
        - If there are no zero or positives, there are no positives.

        """

        def find_first_right(nums, is_on_right: Callable, left=0):
            right = len(nums) - 1

            if is_on_right(nums[left]):
                return left

            if not is_on_right(nums[right]):
                return right + 1

            while True:
                if right - left == 1:
                    return right

                middle = (left + right) // 2
                if is_on_right(nums[middle]):
                    right = middle

                else:
                    left = middle

        first_pos_or_zero = find_first_right(nums, lambda x: x >= 0, 0)
        if first_pos_or_zero == len(nums):
            first_pos = len(nums)

        else:
            first_pos = find_first_right(nums, lambda x: x > 0, first_pos_or_zero)

        neg = max(first_pos_or_zero, 0)
        pos = max(len(nums) - first_pos, 0)
        return max(neg, pos)




