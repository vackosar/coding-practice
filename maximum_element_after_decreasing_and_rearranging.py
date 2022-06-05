from typing import List


# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # I can always array into [1, 2, 3, ..., len(arr)]. That is also the stepest climbing array with maximum value at the end
        # but you cannot calculate how much you can keep increasing without traversing all. This is not enough: min(len(arr), max(1, *arr))
        if len(arr) == 0:
            return 0

        if len(arr) == 1:
            return 1

        arr.sort()
        if arr[0] != 1:
            arr[0] = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1

        return arr[len(arr) - 1]
