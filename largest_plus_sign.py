from typing import List


# https://leetcode.com/problems/largest-plus-sign/
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """
        Cannot brute for as this would be N**3.
        Next to brute force is memorization.
        Potential speedup could be using the mines, but it is not obvious now how to use them.
        Since there is no sort, sort has to be created. To create the sort you have to process all the elements.
        That implies complexity with number of elements.

        For each square calculate maximum possible leg length by counting while reading the matrix and resetting when encountering a mine.
        When going from left, count max leg length to the left, then go from right, then top and bottom.
        Maximum of these is the solution.
        """
