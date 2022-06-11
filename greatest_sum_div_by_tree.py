from typing import List


# https://leetcode.com/problems/greatest-sum-divisible-by-three/submissions/
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # brute force just try all selection - combination number and test divisibility
        # need to test divisibility faster, or need to know what to sum up
        # could find reminders for each - modulo 3, then find combination that gives modulo 0
        # first take all modulo 0
        # then for each modulo 1 you need 2 modulo 1 or one modulo 2. For modulo 2 you need 1 modulo 1 or two modulo 2.
        # sorted from the biggest finding the max it is then just decision between these two options, which ever gives bigger sum, then continue
        # this works because sum of the other two numbers smaller that the current selection, cannot be bigger because we have the sort
        # example 1: [8 (2), 6 (0), 5(2), 3(0), 1(1)] => 3 + 6 + ? from [8(2), 5(2), 1(1)], I take 3 + 6 + 8 + 1
        # Actually this may be wrong and is too complicated. Much simple is to reverse the problem and instead just to find what I need to remove.
        nums.sort()
        mod0 = []
        mod1 = []
        mod2 = []
        self.total = 0
        self.removed = []

        # take 3, do eval of the two choises above
        for current in nums:
            self.total += current
            cm = current % 3
            if cm == 0:
                mod0.append(current)

            elif cm == 1:
                mod1.append(current)

            else:
                mod2.append(current)

        self.sum = self.total

        print(self.removed)
        modulo = self.total % 3
        if modulo == 0:
            return self.total
        
        elif modulo == 1:
            self.pop_one_or_two(mod1, mod2)

        else:
            self.pop_one_or_two(mod2, mod1)

        return self.sum

    def pop_append(self, l: list) -> None:
        i = l.pop(0)
        self.sum -= i
        self.removed.append(i)

    def pop_one_or_two(self, l1, l2):
        if len(l1) >= 1 and len(l2) >= 2:
            if l1[0] <= l2[0] + l2[1]:
                self.pop_append(l1)

            else:
                self.pop_append(l2)
                self.pop_append(l2)

        elif len(l1) >= 1:
            self.pop_append(l1)

        elif len(l2) >= 2:
            self.pop_append(l2)
            self.pop_append(l2)


assert Solution().maxSumDivThree(
    [366, 809, 6, 792, 822, 181, 210, 588, 344, 618, 341, 410, 121, 864, 191, 749, 637, 169, 123, 472, 358, 908, 235,
     914, 322, 946, 738, 754, 908, 272, 267, 326, 587, 267, 803, 281, 586, 707, 94, 627, 724, 469, 568, 57, 103, 984,
     787, 552, 14, 545, 866, 494, 263, 157, 479, 823, 835, 100, 495, 773, 729, 921, 348, 871, 91, 386, 183, 979, 716,
     806, 639, 290, 612, 322, 289, 910, 484, 300, 195, 546, 499, 213, 8, 623, 490, 473, 603, 721, 793, 418, 551, 331,
     598, 670, 960, 483, 154, 317, 834, 352]) == 50487
