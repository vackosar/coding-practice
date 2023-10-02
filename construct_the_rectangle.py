from math import ceil, sqrt
from typing import List


# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        """
        Design a rectangular webpage, whose length is L and width W follows this requirements:
        - L * W = area
        - L >= W
        - abs(L - W) should be as small (close) a as possible.
        - L and W are integrer values.
        Return [L, W]

        >>> Solution().constructRectangle(4)
        [2, 2]

        >>> Solution().constructRectangle(2)
        [2, 1]

        >>> Solution().constructRectangle(7)
        [7, 1]

        >>> Solution().constructRectangle(122122)
        [427, 286]

        We see that because of the integer constraint, this problem has to do with common divisors of the area.

        Simple approach would be to start with L=sqrt(area) and W = sqrt(area) and then iterate to find the integer values that work.
        That is because `sqrt(area) * sqrt(area) == area` at the same time these L and W are the closest to each other, they just may not be integers.
        If we round up (ceil) to nearest higher number that is good first candidate to the most

        There is probably much faster solution using the the common divisors and then split somehow to multiplicators.
        Another interesting solution: https://leetcode.com/problems/construct-the-rectangle/solutions/3562607/python-code-48ms-with-explanation/

        """

        s = ceil(sqrt(area))

        for l in range(s, area + 1):
            if area % l == 0:
                return [l, area // l]

        raise RuntimeError(f"Failed to solve {area}")
