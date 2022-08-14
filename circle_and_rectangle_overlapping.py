import math


class Solution:

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """
        Given circle and a rectangle. Return if they intersect.
        """

        def get_closest(x1, x2, x):
            return min(max(x1, x), x2)

        # find the closest points
        x = get_closest(x1, x2, xCenter)
        y = get_closest(y1, y2, yCenter)

        return radius ** 2 >= (x - xCenter) ** 2 + (y - yCenter) ** 2


assert not Solution().checkOverlap(1, 1, 1, 1, -3, 2, -1)
