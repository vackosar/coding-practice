# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode.com/problems/insert-into-a-binary-search-tree/
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return TreeNode(val)

        node = root
        while True:
            if node.val >= val:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root

                else:
                    node = node.left
                    continue

            elif node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root

                else:
                    node = node.right
                    continue