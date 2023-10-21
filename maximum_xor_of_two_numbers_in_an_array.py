from typing import List


# TODO: finish

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        You are given non-empty positive integer array `nums`.
        Return maximum nums[i] XOR nums[j], where 0 <= i <= j < n.

        XOR is a bit-wise or logical operation, that is the same as OR except for input (1, 1):


        >>> 0 ^ 0
        0

        >>> 1 ^ 0
        1

        >>> 0 ^ 1
        1

        >>> 1 ^ 1
        0

        1 = 01
        2 = 10
        3 = 11
        >>> 2 ^ 1
        3

        >>> 3 ^ 0
        3


        1 = 0001
        5 = 0101
        >>> 5 ^ 1
        4

        5 = 0101
        >>> 5 ^ 5
        0

        1 = 0001
        8 = 1000
        >>> 8 ^ 1
        9

        From above we can see that XOR can also lead to decrease of the larger value.

        So to get the biggest value, we want the highest bit 1, and then the others if possible too.
        That brings us to the examples:

        1 = 0001
        5 = 0101
        8 = 1000
        >>> Solution([1, 5, 8])
        12

        1 = 0001
        5 = 0101
        5 = 0101
        >>> Solution([1, 5, 5])
        4


        Brute force would be N**2 in time.

        Faster solution ideally involves some sort of sorted search or backtracking.
        We want to preserve the highest order bits, but sometimes we have no choice and may have to focus on the lower bits.
        We could always start trying to combine one top-bit number with the next highest bit numbers, which always will be bigger than combining 2 highest order bit numbers.
        If there are no lower bit numbers, only then we would select some other higher order bit. We would pop the highest bit and perform the indentical decision on that level.
        This recursion would lead to a solution of around N*logN speed.

        """
        pass