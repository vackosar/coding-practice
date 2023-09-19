from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Given `grid` matrix of shape (n, n) in a list of rows.
        Return the aggregate largest values in a sliding window of (3, 3) in matrix of (n-2,n-2).
        In another word, find the largest value in each position of 3x3 window (e.g. (1,1), or (2, 3), ...) across the matrix and return it.

        The simplest approach is to iterate over the window positions.

        >>> Solution().largestLocal([[1,2,3],[4,5,6],[7,8,9]])
        [[9]]

        >>> Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
        [[9, 9], [8, 6]]

        >>> Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        """

        n = len(grid)

        output = []
        for i in range(n - 2):
            output.append(list(range(n - 2)))

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                max_val = max(
                    max(grid[i - 1][j - 1:j + 2]),
                    max(grid[i    ][j - 1:j + 2]),
                    max(grid[i + 1][j - 1:j + 2])
                )
                output[i - 1][j - 1] = max_val

        return output

