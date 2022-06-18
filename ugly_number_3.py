# https://leetcode.com/problems/ugly-number-iii/submissions/
from math import gcd, lcm, floor
from typing import Callable


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        ungly =positive integer divisible by a, b, or c
        given n, a, b, c return nth ugly number

        each multiplication is bigger or the same
        a <= b : a * b >= b because a >= 1.
        a <= b does not imply a**2 <= a * b but not a**2 ? b

        Input: n = 3, a = 2, b = 3, c = 5
        (2, 3, 2*2, 5, 2*3, 2*2*2, 3*3, 2*5, )

        I could look what can I multiply with.
        Or I could just do modulo for each integer and look for next.

        # Brute Force 1:

        num = 1
        n_ugly = 0
        while True:
            if num % a == 0 or num % b == 0 or num % c == 0:
                n_ugly += 1
                if n_ugly == n:
                    return num

            num += 1


        # Brute Force 2
        Keep integers that I multiplied with a, b, c and keep increasing.

        a_m = 1
        b_m = 1
        c_m = 1
        n_ugly = 0
        prev = 0
        while True:
            r = min(a_m * a, b_m * b, c_m * c)
            if a_m * a == r:
                a_m += 1

            elif b_m * b == r:
                b_m += 1

            elif c_m * c == r:
                c_m += 1

            if prev != r:
                n_ugly += 1
                if n_ugly == n:
                    return r

            prev = r

        # Binary Search Using Division
        n is divisible by a if n % a == 0 bc (1 * a, 2*a, ...) and count is n / a.
        n is divisible by a and b if n % lcm(a, b) == n % (a * b / gcd(a, b))
        n count of divisible numbers = n / lcm(a,b)
        a union b = a union b minus (a intersect b)
        Inclusion-exclusion principle: |a union b union c| = |a union b union c| - |a intersect b| - |a intersect c| - |b intersect c| + |a intersect b intersect c|
        Define `f(n)` as number of divisions of a or b or c`, so `f(n) := n / lcm(a, b, c) - n / lcm(a, b) - n / lcm(a, c) - n / lcm(b, c) + n / lcm(a, b, c)`
        To find n-th number that is divisible by a, b, or c, use `f` that tells us how many divisible are smaller.
        This is non decreasing function, so can use binary search to find k where `f(k) = n` and `f(k - 1) <= n`.
        Start with min(a,b,c) * k, and search lower.
        """
        high = min(a, b, c) * n
        low = min(a, b, c)
        lcm_ab = lcm(a, b)
        lcm_ac = lcm(a, c)
        lcm_bc = lcm(b, c)
        lcm_abc = lcm(a, b, c)


        # using lambdas, which is slower, but easier to read, could inline for speed

        def num_of_divs(mid):
            return mid // a + mid // b + mid // c - mid // lcm_ab - mid // lcm_ac - mid // lcm_bc + mid // lcm_abc

        def smaller_or_equal_than_target(mid):
            return num_of_divs(mid) >= n

        return self.binary_search(high, low, smaller_or_equal_than_target)

    def binary_search(self, high, low, smaller_or_equal_than_target):
        assert low <= high
        while True:
            if high == low:
                return low

            else:
                mid = (low + high) // 2
                if smaller_or_equal_than_target(mid):
                    high = mid

                else:
                    low = mid + 1


assert Solution().nthUglyNumber(4, 2, 3, 4) == 6
assert Solution().nthUglyNumber(3, 2, 3, 5) == 4
