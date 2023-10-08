from typing import List

# # Simple With Unit Tests for a Quick Understanding
# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        You are given array of integers. Return True if it is a valid mountain array.

        Moutain array is array that:
        - len(arr) >= 3
        - There is `i` that is larger than all valus on the left or right. And the values increase stricly monotonically from the left and decrease stricly monotonically on the right.

        # Examples:

        >>> Solution().validMountainArray([1, 1])
        False

        >>> Solution().validMountainArray([1, 1, 1])
        False

        >>> Solution().validMountainArray([1, 2, 1])
        True

        >>> Solution().validMountainArray([1, 2, 3])
        False

        >>> Solution().validMountainArray([1, 3, 5, 4])
        True

        # peak is the last
        >>> Solution().validMountainArray([1, 3, 5, 4, 6])
        False

        # peak is the first
        >>> Solution().validMountainArray([6, 3, 1])
        False

        # High-level contraints:
        - I can reply true only if I see all the values. There are no guarantees on the input. So the time complexity is at least O(N).
        - I must find one value smaller than the peak on both sides. So the peak must not be first value or the last value.

        # Approaches:
        - The simplest solution is to iterate and validate the condition by keep state if we are before or after the peak.
        The peak candidate is the last value, after which there is strict decline.

        """

        if len(arr) < 3:
            return False

        peak_value = None
        last_value = arr[0]
        for value in arr[1:]:
            if last_value == value:
                return False

            if peak_value is None and last_value > value:
                peak_value = last_value
                if peak_value == arr[0]:
                    return False

            elif peak_value is not None and last_value < value:
                return False

            last_value = value

        return peak_value is not None
