from typing import List


## Follow me for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Calculate the surface of the largest triangle from 3 points on 2-D plain from the list.

        Triangle size is height/2 * b. Height is perpendicular to on the b side and touches the vertex.
        There is a formula for triangle from coordinates also called determinant: `A = (1/2) |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|`

        The simplest solution is iterating over all combinations with time complexity of O(N**3).
        There are more complex solutions involving Gift Wrapping Algorithms.

        >>> Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
        2.0

        >>> Solution().largestTriangleArea([[1,0],[0,0],[0,1]])
        0.5

        >>> Solution().largestTriangleArea([[1,0],[0,0]])
        0.0

        >>> Solution().largestTriangleArea([[1,0],[0,0], [0,0]])
        0.0

        """

        if len(points) < 3:
            return 0.0

        max_area = 0.0
        for (x1, y1) in points:
            for (x2, y2) in points:
                for (x3, y3) in points:
                    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
                    if area > max_area:
                        max_area = area

        return max_area

