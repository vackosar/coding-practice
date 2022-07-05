from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        # https://leetcode.com/problems/largest-number/solution/

        List of non-negative integers. Arrange them to form the largest number and return it as a string.

        If all the integers where max one digit size, then it would mean just sorting from biggest to smallest.
        But we have varying digit length. At the same time, strictly the largest first digit forces the integer selection.

        First we need to think about how we will be constructing the string.
        The simplest way to think about is to work from the lowest part to the biggest,
        If we build from the lowest digits, we don't have to think about changing meaning of digit due to appending integers of different length.

        How to then select the right integer?
        We need integer X, such that if we concat any other integer before it, we will produce bigger number, than if we put the integer X before that integer.
        Once we have this we can repeat the process, but at that point we can ignore the previous step as we already selected the best lowest digits.

        For above comparison to actually make any sense it must have transitive property. The proof of transitivity can be found here:
        https://leetcode.com/problems/largest-number/discuss/291988/A-Proof-of-the-Concatenation-Comparator's-Transtivity

        Ok, now we know we can, let's do this.
        """

        nums = [str(n) for n in nums]

        def compare(x: str, y: str) -> int:
            return int(x + y) - int(y + x)

        nums.sort(key=cmp_to_key(compare), reverse=True)

        # if all are zero iff highest is zero, then need to return zero
        if nums[0] == '0':
            return '0'

        return ''.join(nums)

