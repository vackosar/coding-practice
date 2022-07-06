# https://leetcode.com/problems/count-sub-islands/
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        Two m x n binary matricies grid1 and grid2. Both contain only 0s for water and 1s for land.
        Island is a group of 1s that connects vertically and horizontally with other land that is part of it.
        There are no requirements for size, so even isolated land can be an island.
        Islands in grid2 are sub-islands iff there is an island in grid1 that contains all cells that make up the island in grid2.
        Return number of sub-islands in grid2.

        So the land in the grid2 is split into sub-island land and non-sub-island land.
        First we need to be able to itemize islands in grid2.
        Then it is enough to check for each if all their elements are also land in grid1.

        Finding which elements form together an island requires complexity of at least M * N.
        To check if the islands are sub-islands compute-efficiently will likely require additional storage of M*N.

        Keep current island number which starts from 2 to not collide with unmarked land number 1.
        Iterating element from the top to right and then down.
        If finding unmarked land, then "floodfill" recurse into all 4 directions from that position, while marking unmarked land with island index.
        Store indices of found island land.
        Once we have full island, verify if island elements are sub island.
        To speed up this, we can verify that on the go during the floodfill.
        """

        island_index = 2
        sub_island_count = 0

        if len(grid2) == 0 and len(grid2[0]) == 0:
            return 0

        def mark_land(i, j):
            may_be_sub = True
            if grid2[i][j] == 1:
                grid2[i][j] = island_index
                may_be_sub &= grid1[i][j] == 1

                if i < len(grid2) - 1 and grid2[i + 1][j] == 1:
                    may_be_sub &= mark_land(i + 1, j)

                if j < len(grid2[i]) - 1 and grid2[i][j + 1] == 1:
                    may_be_sub &= mark_land(i, j + 1)

                if i > 0 and grid2[i - 1][j] == 1:
                    may_be_sub &= mark_land(i - 1, j)

                if j > 0 and grid2[i][j - 1] == 1:
                    may_be_sub &= mark_land(i, j - 1)

            return may_be_sub

        # row
        for i in range(len(grid2)):
            # column
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    if mark_land(i, j):
                        sub_island_count += 1

        return sub_island_count


assert Solution().countSubIslands([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
                                  [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0],
                                   [0, 1, 0, 1, 0]]) == 3
