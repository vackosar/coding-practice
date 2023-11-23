import heapq

from utils import NAryTreeNode


class Solution:
    def diameter(self, root: 'NAryTreeNode') -> int:
        """
        Given a n-ary tree returns the length of the diameter of the tree.

        Binary tree has always 2 children. N-ary tree can have multiple children.
        The path may go through the root
        The path any path, including paths that intersect themselves.


        # Examples

        Representation uses None as a separator.

        # Longest shortest path of 3 here is between (2, 5) or (4, 5).
        >>> Solution().diameter(NAryTreeNode.from_list([1, None, 3, 2, 4, None, 5, 6]))
        3

        >>> Solution().diameter(NAryTreeNode.from_list([1, None, 2, None, 3, 4, None, 5, None, 6]))
        4

        >>> Solution().diameter(NAryTreeNode.from_list([1]))
        0

        >>> Solution().diameter(NAryTreeNode.from_list([3, None, 1, None, 5]))
        2


        # What is irrelevant, risk, another unknown?

        Do not only focus on the shortest path between any two nodes in the tree.
        The node values do not matter.


        # Comparison of Extreme Approaches To Find The Best Solution

        - Find the shortest path between all nodes. Complexity O(N**2).
        - The paths cannot intersect itself. It can go through the root.
        - To break the problem down, traverse the tree and do the same for each node recursively.
          Avoid intersecting the path.
          Return the longest path in the subtree, and longest branch in the subtree.
          Once we have the values of lengths for root we are done.
          A leaf does not have two paths, so they can be returned both as zero.


        # Implementation
        """

        def get_two_longest(node: NAryTreeNode):
            if node.children is None or len(node.children) == 0:
                return 0, 0

            longest_sub_branches = []
            longest_sub_paths = []
            for child in node.children:
                longest_sub_branch, longest_sub_path = get_two_longest(child)
                longest_sub_branches.append(longest_sub_branch)
                longest_sub_paths.append(longest_sub_path)

            longest_sub_branches = heapq.nlargest(2, longest_sub_branches)
            longest_sub_path = max(longest_sub_paths)
            longest_sub_branches = [i + 1 for i in longest_sub_branches]

            if len(longest_sub_branches) == 1:
                longest_path = max(longest_sub_path, longest_sub_branches[0])

            else:
                longest_path = max(longest_sub_branches[0] + longest_sub_branches[1], longest_sub_branches[0], longest_sub_path)

            return longest_sub_branches[0], longest_path

        longest_sub_branch, longest_path = get_two_longest(root)

        return longest_path



