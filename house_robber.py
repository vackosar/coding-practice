from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/house-robber/

        Nodes in a line.
        Each node has some known amount.
        Cannot visit two adjacent nodes.
        Find the maximum amount that can be gained.

        # Brute force
        Try out all possible visits by depth first search.
        This is O(N!) complexity.

        # Greedy
        Each decision blocks the nearby nodes.
        So value of that node in each point is the value of the node minus the neighbors.
        Select the max from all these at each time.
        Keep track which nodes can still be selected and which neighbors are already blocked.
        On removal update all neighbors which will have some opportunity cost amortized.
        With doubly linked list and a heap this should be O(N Log N), as we need to remove and reinsert the second neighbors.

        # Dynamic programming
        Calculate table of corresponding decisions.
        Based on previous decision we can make only some decisions.
        Not visiting the current node, allows us to choose the maximum both of the pasts the bigger.
        Vising the current node, only valid choice of the past is not visiting.
        Since we can decide this in forward pass, depending only on the previous node results, and selecting the best.
        This can be solved in O(N) time and O(1) space.

        """

        previous_visit_no = 0
        previous_visit_yes = 0

        for node_amount in nums:
            visit_no = max(previous_visit_yes, previous_visit_no)
            visit_yes = previous_visit_no + node_amount

            previous_visit_no = visit_no
            previous_visit_yes = visit_yes

        return max(previous_visit_yes, previous_visit_no)

