# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]

        while len(queue) > 0:
            node = queue.pop()
            if node is not None:
                node.right, node.left = node.left, node.right
                queue.extend([node.left, node.right])

        return root
