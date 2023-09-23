from typing import Optional

from utils import TreeNode


## Follow me for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Find the length of the shortest paths to a leaf node.
        In other words, find a distance of nearest to root.
        Single root node is a 1 step from leaf.
        But if the root has any leaf, you count that.

        >>> Solution().minDepth(TreeNode.from_level_order_list([0, None, None]))
        1

        >>> Solution().minDepth(TreeNode.from_level_order_list([0, None, 1]))
        2

        >>> Solution().minDepth(TreeNode.from_level_order_list([3, 9, 20, None, None, 15, 7]))
        2


        We know that the contents are sorted.
        If we knew that the contents are all integers, this could give us hints which branches are more promising.
        But this is not explicitly defined.

        So the shortest path has to be found via bredth-first, level-by-level.
        Calculate depth from the current level, find minimum.

        Recursively, the solution is O(N) memory and compute with extra spending on the stack.
        We could do it O(log(N)) by iterative approach.
        """

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        elif root.left is None:
            return self.minDepth(root.right) + 1

        elif root.right is None:
            return self.minDepth(root.left) + 1

        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

