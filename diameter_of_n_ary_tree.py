from utils import NAryTreeNode


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


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

            # Initialize these to 0 to handle the case where there are fewer than two children
            first_longest = second_longest = 0
            longest_sub_path = 0

            for child in node.children:
                longest_sub_branch, longest_sub_path_child = get_two_longest(child)

                if longest_sub_branch + 1 > first_longest:
                    second_longest = first_longest
                    first_longest = longest_sub_branch + 1
                elif longest_sub_branch + 1 > second_longest:
                    second_longest = longest_sub_branch + 1

                # Find the maximum sub-path among children
                longest_sub_path = max(longest_sub_path, longest_sub_path_child)

            # Calculate the longest path that includes this node by considering two largest children branches
            longest_path = max(first_longest + second_longest, longest_sub_path)

            return first_longest, longest_path

        longest_sub_branch, longest_path = get_two_longest(root)
        return longest_path


