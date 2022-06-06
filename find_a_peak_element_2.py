from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        brute force: iterate over i, j in [1 to len() - 1, 1 to len()] is N**2.
        Sort is n log n, so this wont be based on sort.
        Only algos can can halven the intervals are log n. Sort is n log n
        So this may be about iterating over rows, and then halving the intervals in some way, but how?
        There may be only one local peak if it is also a global peak.
            Thanks to the local condition and -1 perimeter, it must be also a local peak if it is a biggest number in 3 columns.
            In that case how to find it in less than N**2?
            Only way to find it is using the local condition, that tell us that any maximum is either a peak or shows the path towards it.
            So we need to do the max on 3 columns and either stop or go split towards to max.
        """
        # TODO
