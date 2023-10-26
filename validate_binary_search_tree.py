# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from utils import TreeNode


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        You are given a binary tree.
        Return True if the tree is a valid tree.

        A binary tree is valid if
        - the left subtree values are less,
        - and the right subtree values are more than the root value,
        - and all subtrees are valid.

        >>> Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
        True

        >>> Solution().isValidBST(TreeNode(1, TreeNode(2), TreeNode(3)))
        False

        >>> Solution().isValidBST(TreeNode(2, TreeNode(-1), TreeNode(4, TreeNode(3), TreeNode(5))))
        True

        >>> Solution().isValidBST(TreeNode(2, TreeNode(-1), TreeNode(4, TreeNode(1), TreeNode(5))))
        False

        >>> Solution().isValidBST(TreeNode(2, TreeNode(-1, TreeNode(0)), TreeNode(4, TreeNode(3), TreeNode(5))))
        False


        If root of the left subtree is less, all the values in the left of that subtree will be also less.
        But we cannot say that about the right subtree of the left subtree without explicitly comparing with the root value.
        So to verify we need to effectively keep a minimum of the visited root values and make sure that all right values on the left are less.

        A similar problem occurs for the right subtree of the root and its left values.

        In general, we will have an interval of allowed values for each subtree and will be comparing with it and updating it during the recursion.

        This solution will O(N) time, but also O(N) space.
        """

        def isValidSubTree(root: TreeNode, min_val: Optional[int], max_val: Optional[int]):
            if root.left is not None:
                if root.left.val >= root.val or min_val is not None and root.left.val <= min_val:
                    return False

                if not isValidSubTree(root.left, min_val, root.val):
                    return False

            if root.right is not None:
                if root.right.val <= root.val or max_val is not None and root.right.val >= max_val:
                    return False

                if not isValidSubTree(root.right, root.val, max_val):
                    return False

            return True

        if root is None:
            return True

        return isValidSubTree(root, None, None)
