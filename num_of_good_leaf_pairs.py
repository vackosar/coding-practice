# Definition for a binary tree node.
from typing import List

from utils import TreeNode


# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Given root, integer distance.
        Pair of leaf nodes is good if path between is shorter than distance.
        Return number of good pairs.
        root = [1, 2, 3, null, 4] distance = 3 results in 1 (just one leaf pair distance 3)

        [1, 2, 3, 4, 5, 6, 7] results in 2


        # Brute force:
        Stack of all leafs. Pop one, explore distance leaf neighbors, add count, loop. For this have to keep path to parents.
        Complexity N * distance.
        Problem here is keeping path to parent. It is difficult to not overwrite, so easiest is to .


        # Recursive?
        - counting how many distances to leafs under both nodes. Adding to count those that can connect.
        - N * (problem of matching distances) but higher memory complexity.
        Would have to store the results in count * distance array. Prevent matching within on result.


        Below is the Brute Force approach.
        """
        self.count = 0
        self.distance = distance
        self.find_leafs(root, [])
        assert self.count % 2 == 0
        return self.count // 2

    def find_leafs(self, node: TreeNode, path: list):
        path = list(path)
        if node.left is None and node.right is None and len(path) > 0:
            self.search_neighbors(node, path[-1], path[:-1], self.distance - 1)

        if node.left is not None or node.right is not None:
            path.append(node)

        if node.left is not None:
            self.find_leafs(node.left, path)

        if node.right is not None:
            self.find_leafs(node.right, path)

    def search_neighbors(self, prev_node: TreeNode, node: TreeNode, path: list, distance: int):
        # cannot search parents, as don't have a link to them, woudl have to hand it over
        if node.left is None and node.right is None:
            # we arrived to a leaf, so must have come from the parent, distance must be at least zero. So add.
            self.count += 1

        elif distance >= 1:
            # need to make at least one mrore step, but not back.

            if node.right != prev_node and node.right is not None:
                cpath = list(path)
                cpath.append(node)
                self.search_neighbors(node, node.right, cpath, distance - 1)

            if node.left != prev_node and node.left is not None:
                cpath = list(path)
                cpath.append(node)
                self.search_neighbors(node, node.left, cpath, distance - 1)

            if len(path) > 0 and path[-1] != prev_node:
                self.search_neighbors(node, path[-1], list(path)[:-1], distance - 1)


assert Solution().countPairs(TreeNode.from_level_order_list([100]), 3) == 0
assert Solution().countPairs(TreeNode.from_level_order_list([1, 2, 3, None, 4]), 3) == 1
assert Solution().countPairs(TreeNode.from_level_order_list([1, 2, 3, 4, 5, 6, 7]), 3) == 2
assert Solution().countPairs(TreeNode.from_level_order_list([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]), 3) == 1
