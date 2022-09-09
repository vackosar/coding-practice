class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

        Given 3 positive integers,
        return minimum flips required for  `a bitwise_or b == c`

        Since this problem is entirely bit-wise,
        I just need to iterate and solve 3 possible cases for each bit and count the flips needed,
        and I will get linear O(bit_count) solution with constant space O(C).
        The only issue is getting the bit array.

        This program speed is very sensitive on specific operations used.
        For example comparison bigger than zero is slower than test for non zero.
        Reminder after division is slower than bit-and operation with 1.

        """

        n_flips = 0
        while a or b or c:
            # lowest bit
            bit_a, bit_b, bit_c = a & 1, b & 1, c & 1

            # the cases
            if bit_a == 0 and bit_b == 0 and bit_c == 1:
                n_flips += 1

            elif ((bit_a == 1 and bit_b == 0) or (bit_a == 0 and bit_b == 1)) and bit_c == 0:
                n_flips += 1

            elif (bit_a == 1 and bit_b == 1) and bit_c == 0:
                n_flips += 2

            # shift bits left, and iterate
            a = a >> 1
            b = b >> 1
            c = c >> 1

        return n_flips


assert Solution().minFlips(2, 6, 5) == 3
