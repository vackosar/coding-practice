from typing import List


## Follow me for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        Input is matrix of (m, n) of distinct numb ers, return all lucky numbers in any order.
        A lucky number is minimum in its row and max in its column.

        >>> Solution().luckyNumbers([[1, 2, 3], [-1, -1, -1], [-1, -1, -1]])
        [1]

        >>> Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])
        [12]

        >>> Solution().luckyNumbers([[7,8],[1,2]])
        [7]


        The simplest would be to brute force.
        The second simplest would be to find first the maximums and minimums and find indexes where these match.
        Because the values are distinct, we don't have to worry about multiple maximums.

        """

        row_min_idxs = []
        results = []

        for i, row in enumerate(matrix):
            row_min = None
            row_min_j = None
            for j, val in enumerate(row):
                if row_min is None or val < row_min:
                    row_min_j = j
                    row_min = val

            row_min_idxs.append([i, row_min_j])

        for j in range(len(matrix[0])):
            col_max = None
            col_max_i = None
            for i, row in enumerate(matrix):
                val = matrix[i][j]
                if col_max is None or val > col_max:
                    col_max_i = i
                    col_max = val

            if [col_max_i, j] in row_min_idxs:
                results.append([col_max_i, j])

        return [matrix[i][j] for i, j in results]
