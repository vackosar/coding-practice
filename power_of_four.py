from math import log


# Simplest Solution with Unit Tests and Alternatives
## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Given `n` integer between 2**-31 and 2**31 - 1. Return True when `n` is power of four.

        >>> Solution().isPowerOfFour(4)
        True

        >>> Solution().isPowerOfFour(1)
        True

        >>> Solution().isPowerOfFour(4)
        True

        >>> Solution().isPowerOfFour(0)
        False

        >>> Solution().isPowerOfFour(-1)
        False

        >>> Solution().isPowerOfFour(16)
        True

        >>> Solution().isPowerOfFour(-4)
        False

        Because `n` is integer we cannot get n == 4**(-2), which would be non-integer.


        There could be path through divisors, but I am not familiar with these methods and it could be slow.

        Since there are not that many powers of 4 in provided range, we could just enumerate into a static constant and check that.

        Because the `n` cannot be too large I could take brute force approach for simply exponentiating.

        ```
        while True:
            # c = c * 4
            c = c << 2
            if c == n:
                return True

            elif c > n:
                return False
        ```

        Another faster approach is use the inverse operation to power (or exponentiation), which is log-4.

        Another faster approach is use bit shift by 2 steps to quickly simulate multiplication with 4 without multiplication itself.

        Since we now see that this is easily checked in bit-representation. We can check that if we substract one, that we will get number that has bit representation that ones only on places where the other does not, which can happen only if our number has a single one in the bit representation. The check can be done with bit-and with the original it would return zero.

        Here is list of other cool solutions: https://leetcode.com/problems/power-of-four/solutions/2461223/python-99-no-more-loop-or-recursion-one-liner-with-detailed-explanation-and-different-approach/

        """

        if n < 1:
            return False

        if n == 1:
            return True

        return log(n, 4).is_integer()


