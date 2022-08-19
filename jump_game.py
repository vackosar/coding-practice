from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/jump-game/submissions/
        
        You start at index 0. You need to get to the last index len(nums) - 1.
        The nums array gives you maximum jump length at each position.
        Return true if the last index can be reached.

        Interate over the indexes from left to right, marking an array which indexes are reachable.
        Stop if the next node is not reachable or if at the last index.
        Complexity O(N), O(N).

        Instead of marking all reachable, just keep the maximum reachable index at each step.
        Complexity O(N), O(1)
        """

        max_reachable = 0
        for i, current_max_jump in enumerate(nums):
            if i > max_reachable:
                return False

            max_reachable = max(i + current_max_jump, max_reachable)

        return True
