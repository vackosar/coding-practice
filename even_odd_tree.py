from typing import Optional

from utils import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        https://leetcode.com/problems/even-odd-tree/

        Input is a binary tree.
        Return True if the tree is Even-Odd, otherwise return False.
        Level is number of ancestors towards the root. Where root has 0 ancestors. The root's children have 1 ancestor.
        Even-Odd is defined with following:
        - Parent are the nodes closer to the root i.e. at lower level.
        - At even-indexed level, all nodes are odd integer values, sorted strictly increasing from the left to the right.
        - At odd-indexed level, all nodes are even integer valeus, strictly decreasing from the left to the right.


        # BFS with a Level Marker

        Queue with each node to be processed to have a marker, which level it is from to switch between the rules.
        Complexity time O(N), memory O(log(N)).

        """

        # FIFO queue for BFS
        # root at level 0
        queue = [(root, 0)]
        prev_node = None
        prev_level = -1

        while queue:
            node, level = queue.pop(0)

            if level % 2 == 0:
                # even
                if node.val % 2 == 0:
                    return False

                if prev_level == level and prev_node.val >= node.val:
                    return False

            else:
                # odd
                if node.val % 2 == 1:
                    return False

                if prev_level == level and prev_node.val <= node.val:
                    return False

            if node.left is not None:
                queue.append((node.left, level + 1))

            if node.right is not None:
                queue.append((node.right, level + 1))

            prev_node = node
            prev_level = level

        return True


assert Solution().isEvenOddTree(
    TreeNode.from_level_order_list([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2])) == True
