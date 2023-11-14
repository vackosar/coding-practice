# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        """
        Input is two positive integers.
        Consider set of integers `nums` where:
        - The units digit (lowest digit in decimal representation) of each of nums is k.
        - The sum of the integers nums is num.

        The set can contain multiple of the same integers, and sum of an empty se is 0.

        Return the minimum possible size of such a set, or -1 if no such set exists.


        # Examples with Edge Cases

        # [29, 29] or [9, 49]
        >>> Solution().minimumNumbers(58, 9)
        2

        # The sum of even numbers is always even
        >>> Solution().minimumNumbers(37, 2)
        -1

        # The empty set gives 0.
        >>> Solution().minimumNumbers(0, 7)
        0

        >>> Solution().minimumNumbers(1, 1)
        1

        # [1, 1, 11]
        >>> Solution().minimumNumbers(13, 1)
        3

        >>> Solution().minimumNumbers(1, 1)
        1


        # Contrast The Extreme Approaches

        Focus on the first decimal. Iterate over mulpliers of the `k` looking for modulo 0.
        The time complexity is linear and memory is constant.


        # Risks
        This could fail if my intution about the higher digits is wrong.


        # Implementation

        """

        if num == 0:
            return 0

        ld = num % 10

        for i in range(1, num + 1):
            # multiply to see what lowest digit we get from the modulo
            lsum = i * k

            if lsum > num:
                # the num is too large, there is no way to do this
                return -1

            if lsum % 10 == ld:
                # The first that match is the one. Because I can match the rest of the digits in the sum
                return i

        return -1
