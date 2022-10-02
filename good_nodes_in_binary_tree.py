from tree_iterator import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # https://leetcode.com/problems/count-good-nodes-in-binary-tree/
        # I can use backtracking with depth first search
        # can recursively travel the tree and check the condition by keeping max value
        # actually I must crawl all nodes as there is no sort
        if root is None:
            return 0

        else:
            return 1 + self.n_good_nodes(root.left, root.val) + self.n_good_nodes(root.right, root.val)

    def n_good_nodes(self, node, max_val) -> int:
        if node is None:
            return 0

        good_count = 0
        if node.val >= max_val:
            good_count += 1

        max_val = max(node.val, max_val)
        good_count += self.n_good_nodes(node.left, max_val)
        good_count += self.n_good_nodes(node.right, max_val)
        return good_count


