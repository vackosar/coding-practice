from math import floor, ceil
from typing import List


# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
# better solution https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/discuss/999257/C%2B%2BJavaPython-O(n)-with-picture
    # just remember that moving l to right can only mean increase in both min_r and max_r. So you can store progress in those.
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        split into non empty where sum(left) <= sum(mid) <= sum(right)
        brute force: try to split all combinations, can use cumulative sum to get the partial sums, so all splits is N**2
        apparently left most + right most
        when searching for the right position


        Stopping condition search interval is size 1, then decide if found solution or no solution exists.
        you have 2 conditions for splitting
        1 - the middle sum is bigger than left sum
        2 - the middle sum is smaller than right sum
        If both true go left - reset search right boundary to the current position
        If 1 is not true go right
        If 2 is not true go left
        If both not true stop



        """

        csum = []
        for i in range(len(nums)):
            csum.append(sum(nums[:i + 1]))

        self.csum = csum
        solutions = []

        # index means after this there is the separation
        # csum is a sorted array, so can binary search
        n_solutions = 0
        for l in range(len(nums) - 1):

            r_search_l = l + 1
            r_search_r = (len(csum) - 2)
            if not self.middle_vs_right(l, r_search_l):
                continue

            if not self.left_vs_middle(l, r_search_r):
                continue

            min_r = self.search(nums, l, r_search_l, r_search_r, go_left=True)
            if min_r is None:
                continue

            max_r = self.search(nums, l, r_search_l, r_search_r, go_left=False)
            if max_r is None:
                continue

            n_solutions += max_r - min_r + 1

        return n_solutions

    def search(self, nums, l, r_search_l, r_search_r, go_left):
        # l = 1
        while True:
            current_r = (r_search_r + r_search_l) / 2
            if go_left:
                current_r = floor(current_r)

            else:
                current_r = ceil(current_r)

            is_lm = self.left_vs_middle(l, current_r)
            is_mr = self.middle_vs_right(l, current_r)
            is_last = r_search_r - r_search_l == 0

            if not is_lm and not is_mr:
                break

            elif not is_lm and is_mr:
                if is_last:
                    break

                r_search_l = current_r + 1

            elif is_lm and not is_mr:
                if is_last:
                    break

                r_search_r = current_r - 1

            else:
                # default go left
                if is_last:
                    # print(go_left, nums[0:l + 1], nums[l + 1: current_r + 1], nums[current_r + 1:])
                    # solutions.append((l, current_r))
                    return current_r

                if go_left:
                    r_search_r = current_r

                else:
                    r_search_l = current_r

        return None

    def left_vs_middle(self, l, r):
        return self.csum[l] <= self.csum[r] - self.csum[l]

    def middle_vs_right(self, l, r):
        return self.csum[r] - self.csum[l] <= self.csum[len(self.csum) - 1] - self.csum[r]


assert Solution().waysToSplit([1, 1, 1]) == 1
assert Solution().waysToSplit([1, 2, 2, 2, 5, 0]) == 3
