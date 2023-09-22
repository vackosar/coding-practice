## Follow me for more software and machine learning at https://vaclavkosar.com/

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        """
        Given (n,n) square image, flip it horizonatally, invert it (1-x) and return result.

        >>> Solution().flipAndInvertImage([[1,1,0]])
        [[0, 0, 1]]

        >>> Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 1]])
        [[1, 0, 0], [0, 1, 0], [0, 1, 1]]

        >>> Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
        [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

        Simply reverse each row, and invert the value, return results.
        Complexity O(n**2).

        Memory complexity can be reduced by reusing the input matrix.

        """

        return [
            [1 - x for x in reversed(row)]
            for row in image
        ]