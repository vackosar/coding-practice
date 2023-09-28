from typing import Optional

from utils import TreeNode


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Sum all the left leaves. That is sum of all left nodes that have no children.


        # Left leaves are 9 + 15.
        >>> Solution().sumOfLeftLeaves(TreeNode.from_level_order_list([3, 9, 20, None, None, 15, 7]))
        24

        # This is not left to any node.
        >>> Solution().sumOfLeftLeaves(TreeNode.from_level_order_list([3]))
        0

        >>> Solution().sumOfLeftLeaves(TreeNode.from_level_order_list([3, 1, None]))
        1

        # No left leaves.
        >>> Solution().sumOfLeftLeaves(TreeNode.from_level_order_list([3, None, 4]))
        0

        """

        left_sum = 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                # We know this is a left leaf, so we add left.val too.
                left_sum += root.left.val

            else:
                left_sum += self.sumOfLeftLeaves(root.left)

        if root.right is not None:
            left_sum += self.sumOfLeftLeaves(root.right)

        # We may know this is a leaf, but don't know if this is a left leaf here.

        return left_sum




