# FIXME


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from utils import TreeNode


class Solution(object):
    def recoverTree(self, root):
        """

        We need to search the corrupted node, which can have only sub-nodes were swapped.
        Depth-first search is simpler and the speed is the same.
        It can be implemented in a recursive manner.


        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.recoverTreeFind(root)
        return root

    def recoverTreeFind(self, root):

        if root is None:
            return False

        elif root.val is None:
            if root.left is not None:
                root.left.val, root.val = root.val, root.left.val
                return True

            elif root.right is not None:
                root.right.val, root.val = root.val, root.right.val
                return True

        elif root.left is not None and root.right is not None and root.left.val > root.right.val:
            # Compare the right and the left first, because otherwise we would swap with the middle incorrectly.
            root.left.val, root.right.val = root.right.val, root.left.val
            return True

        elif root.left is not None and root.left.val is not None and root.left.val > root.val:
            root.left.val, root.val = root.val, root.left.val
            return True

        elif root.right is not None and root.right.val is not None and root.right.val < root.val:
            root.right.val, root.val = root.val, root.right.val
            return True

        else:
            if self.recoverTreeFind(root.left):
                return True

            if self.recoverTreeFind(root.right):
                return True

            # We haven't found the problem in this subtree.
            return False


# assert (Solution()
#         .recoverTree(TreeNode.from_level_order_list([3, 1, 4, None, None, 2]))
#         .to_level_order_list()
#         == [2, 1, 4, None, None, 3])

assert (Solution()
        .recoverTree(TreeNode.from_level_order_list([3, 1, 5, None, None, 4]))
        .to_level_order_list()
        == [3, 1, 5, None, None, 4])


assert (Solution()
        .recoverTree(TreeNode.from_level_order_list([3, 5, 1, None, None, 4]))
        .to_level_order_list()
        == [3, 1, 5, None, None, 4])