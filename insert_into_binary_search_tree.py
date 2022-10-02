# https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import Optional

from utils import TreeNode


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