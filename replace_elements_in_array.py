from typing import List

# https://leetcode.com/problems/replace-elements-in-an-array/submissions/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # brute force solution: just search everytime you pick an operation O(n * m)
        # faster - do some sort on the arrays, but the sort would have to be preserved. I don't think I have binary tree in Python implemented
        # cannot sort operations

        op_map = dict()
        for old, new in reversed(operations):
            if new not in op_map:
                op_map[old] = new

            else:
                last_new = op_map.pop(new)
                op_map[old] = last_new

        result = []
        for n in nums:
            if n not in op_map:
                result.append(n)

            else:
                result.append(op_map[n])

        return result

    def solution1(self, nums, operations):
        # low memory usage
        nm = dict()
        for i, n in enumerate(nums):
            nm[n] = i

        for old, new in operations:
            i = nm.pop(old)
            nums[i] = new
            nm[new] = i
            


assert Solution().arrayChange([1,2,4,6], [[1,3],[4,7],[6,1]]) == [3,2,7,1]