from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # deleted = []
        deleted_count = 0
        # Sort is crutial. Quick sort complexity: O(log n)
        intervals.sort()
        current = intervals[0]
        # iteration O(n)
        for interval in intervals[1:]:
            if interval[0] < current[1]:
                # thanks to the sort all overlapping are here
                # we have to delete some array for each, but which?
                # We have to prioritize those with more overlaps. Thanks to the sort more overlaps will have the interval with interval further to the right.

                if interval[1] > current[1]:
                    # We delete intervals that overlap more other intervals
                    # We keep the current interval.
                    # deleted.append(interval)
                    deleted_count += 1

                elif interval[1] <= current[1]:
                    # we delete the current, and switch to the new
                    # deleted.append(current)
                    current = interval
                    deleted_count += 1

            else:
                # no need to delete anything
                current = interval

        # print(deleted)
        return deleted_count

# Review these solutions as well
# https://leetcode.com/problems/non-overlapping-intervals/discuss/2081336/Python-O(n-log-n)-or-O(1)
# https://leetcode.com/problems/non-overlapping-intervals/discuss/2095068/Easy-Python-solution-with-detailed-explanation


assert Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
