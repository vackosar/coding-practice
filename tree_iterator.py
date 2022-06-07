# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.path = [root]
        self.go_left_most()

    def next(self) -> int:
        current = self.path[-1]
        val = current.val
        if current.right is not None:
            self.path.append(current.right)
            self.go_left_most()

        else:
            self.path.pop()
            while len(self.path) > 0 and self.path[-1].right == current:
                current = self.path.pop()

        return val

    def hasNext(self) -> bool:
        return len(self.path) > 0

    def go_left_most(self):
        while self.path[-1].left is not None:
            self.path.append(self.path[-1].left)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


