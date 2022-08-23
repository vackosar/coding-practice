from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Input is a triangle which has size 1 on the top and is widest on the bottom, growing by one element at each layer.
        Find minimum path from the top to bottom. On each step you can decide which nearby element to visit.
        Return the minimum path sum from the top to the bottom.

        # Brute Force
        Iterate over all possible paths and keep the minimum.

        # Dynamic Programming
        We can evaluate the shortest sums going back from the bottom for each position in the level looking at the lower level.
        Not having to evaluate multiple times the same sub-paths.
        To save memory we store the sums in the triangle itself.

        """

        for level_from_bottom in range(1, len(triangle)):
            level = len(triangle) - 1 - level_from_bottom
            level_arr = triangle[level]
            prev_level_arr = triangle[level + 1]
            for element_index in range(len(level_arr)):
                level_arr[element_index] = level_arr[element_index] + min(prev_level_arr[element_index],
                                                                          prev_level_arr[element_index + 1])

        return triangle[0][0]


# Upvote and follow me at https://vaclavkosar.com/
