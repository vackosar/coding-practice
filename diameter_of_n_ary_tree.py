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
        4

        >>> Solution().diameter(NAryTreeNode.from_list([1, None, 2, None, 3, 4, None, 5, None, 6]))
        6

        >>> Solution().diameter(NAryTreeNode.from_list([1]))
        0

        # What is irrelevant, risk, another unknown?

        Do not only focus on the shortest path between any two nodes in the tree.
        The actual values do not matter.


        # Comparison of Extreme Approaches To Find The Best Solution

        - Find the shortest path between all nodes. Complexity O(N**2).
        - Since the path can intersect itself, it can always go through the root, which is the longest option. Thanks to this we need to only find 2 longest paths from the root. To break the problem down, traverse the tree and do the same for each node recursively. Once we have the values of lengths for root we are done. A leaf does not have two paths, so they can be returned both as zero.
        - TODO Alternative: Avoid intersecting the path: Return the longest path in the subtree, and longest branch in the subtree.

        # Implementation
        """

        def get_two_longest(node: NAryTreeNode):
            if node.children is None or len(node.children) == 0:
                return [0]

            longest = []
            # itertools.chain(two_longest(child) for child in node.children)
            for child in node.children:
                longest.extend(get_two_longest(child))

            longest = heapq.nlargest(2, longest)
            # we made a step up
            longest = [i + 1 for i in longest]
            return longest

        longest = get_two_longest(root)
        if len(longest) == 1:
            return 0

        return longest[0] + longest[1]



