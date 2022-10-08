class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        https://leetcode.com/problems/loud-and-rich/

        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]


        Richer is array of pairs, for which the first element an index of a person is strictly richer than the second index.
        The second array is an array of quietness of each person.

        Return an array answer, where answer[x] = y, when y is the least quiet person among all equally rich or richer than x.


        If two people are of equal wealth there will be no edge between them in richer array.
        For each index find richer or same richness and least quiet.


        # Brute Force
        For each index iterate over itself and richer and find the quitest.


        # Depth First Search on Forest
        Iterate over richer array to build which nodes are smaller.
        Create a result array.
        Start from the quiet array from the left.
        Propogate the smallest to the less rich or itself as notes in the output.
        Stop propagation if lower quiteness is already filled in in the

        """
        richer_than_map = [[] for _ in range(len(quiet))]

        for richer, poorer in richer:
            richer_than_map[richer].append(poorer)

        output = [None] * len(quiet)
        output_q = [None] * len(quiet)

        def recurse(i, q, q_i):
            """
            i: index of the current
            q: quietness of the richer or equal.
            q_i: index of the source of the quietness
            """

            current_q = output_q[i]
            if current_q is None or current_q > q:
                output_q[i] = q
                output[i] = q_i
                for poorer_i in richer_than_map[i]:
                    recurse(poorer_i, q, q_i)

        # Thanks to the sort we are iterating over the most loud first and so recursion will be increasingly shallow.
        for i, q in sorted(((i, quietness) for i, quietness in enumerate(quiet)), key=lambda x: x[1]):
            recurse(i, q, i)

        return output


assert Solution().loudAndRich(
    [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
    [3, 2, 5, 4, 6, 1, 7, 0]) == [5, 5, 2, 5, 4, 5, 6, 7]
