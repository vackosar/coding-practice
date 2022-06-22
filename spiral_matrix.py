from typing import List

# https://leetcode.com/problems/spiral-matrix/submissions/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return matrix elements read in a spiral order.

        Could be just changing the values in the matrix to None and use that to detect already used.
        Alternatively could store level value used to derive the width and height of the current matrix.
        The second option is cleaner.

        Anytime about to exit the matrix need to change direction or stop.
        Position within the matrix could define the direction.
        """

        h = len(matrix)
        if h == 0:
            return []

        w = len(matrix[0])
        r = []

        level = 0
        i, j = 0, 0
        while True:
            r.append(matrix[i][j])

            if i == level and j < w - level - 1:
                j += 1

            elif j == w - level - 1 and i < h - level - 1:
                i += 1

            elif i == h - level - 1 and j > level and h - 2 * level > 1:
                j -= 1

            elif j == level and i > level + 1 and w - 2 * level > 1:
                i -= 1

            elif j == level and i == level + 1 and (w - 2 * (level + 1) > 0 and h - 2 * (level + 1) > 0):
                level += 1
                j += 1

            else:
                return r


assert Solution().spiralOrder([[2, 5], [8, 4], [0, -1]]) == [2, 5, 4, -1, 0, 8]

# assert Solution().spiralOrder([[3],[2]]) == [3, 2]
# assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
