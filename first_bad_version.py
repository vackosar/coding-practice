# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# Simple With Unit Tests for a Quick Understanding
# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


def myIsBadVersion(i: int) -> bool:
    return isBadVersion(i)


class Solution:
    def firstBadVersion(self, n: int, isBadVersion=myIsBadVersion) -> int:
        """
        There were series of n production, where there is a bad version after which all versions are bad.
        You have n versions and want to find the first bad version.
        You can call isBadVersion(version: int) t find out.
        The versions are 1-indexed.


        # Examples
        Unit tests are hard to implement here, because we don't have the isBadVersion method output here.

        # checks: 3, 5, 4, because: we are halving the intervals to find the edge
        >>> Solution().firstBadVersion(5, isBadVersion=lambda i: i >= 4)
        4

        >>> Solution().firstBadVersion(1, isBadVersion=lambda i: i >= 1)
        1

        >>> Solution().firstBadVersion(2, isBadVersion=lambda i: i >= 1)
        1


        # Approaches

        We have elements "sorted" by whether they are bad or not.
        Search is sorted arrays is time complexity Log(N).

        So we can be halving the intervals and quickly find the first bad.
        We keep our version bad and halve to keep it so.
        Each time check the version on the left.

        As an optimization, we could cache the isBad results in a dictionary.

        """

        if n == 1:
            return 1

        # boundaries
        left = 1
        right = n

        if isBadVersion(left):
            return 1

        while True:
            if right - left == 1:
                # right is kept bad and left not
                return right

            version = (right + left) // 2
            if isBadVersion(version):
                # halve left
                right = version

            else:
                if version == n:
                    # this should not happen
                    raise ValueError()

                # halve right
                left = version
