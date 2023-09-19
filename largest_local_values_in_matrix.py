from itertools import product
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Given `grid` matrix of shape (n, n) in a list of rows.
        Return the aggregate largest values in a sliding window of (3, 3) in matrix of (n-2,n-2).
        In another word, find the largest value in each position of 3x3 window (e.g. (1,1), or (2, 3), ...) across the matrix and return it.

        The simplest approach is to iterate over the window positions O(N).

        Ordinary iterating will be slow due to Python. Better is to use comprehensions.

        >>> Solution().largestLocal([[1,2,3],[4,5,6],[7,8,9]])
        [[9]]

        >>> Solution().largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
        [[9, 9], [8, 6]]

        >>> Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        """

        n = len(grid)
        output = [[0] * (n - 2) for _ in range(n - 2)]

        for i, j in product(range(1, n - 1), range(1, n - 1)):
            output[i - 1][j - 1] = max(grid[r][c] for r, c in product(range(i - 1, i + 2), range(j - 1, j + 2)))

        return output

