from math import ceil


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        Input strings are a, b. How many times to repeat `a` such that `b` is a substring of `a`?


        # Pure iteration is to slow O(a * b)!

        if len(b) == 0:
            return 0

        for offset in range(len(a)):
            failed = False
            count = 1
            for i in range(len(b)):
                a_i = (i + offset) % len(a)
                if a[a_i] != b[i]:
                    failed = True
                    break

                # print(a[a_i], b[i])
                if a_i == 0 and i + offset + 1 > len(a):
                    count += 1

            if not failed:
                return count

        return -1



        # Need something faster
        Could find first suffix trie from multiple appends of `a` of max length `b`, then match within that.
        This finds the exact match position, but we don't need that.
        In fact in Python this is a very inefficient as for loops are slow.


        if len(b) == 0:
            return 0

        if len(a) == 0:
            return -1

        n_append = ceil(len(b) / len(a)) + 1
        a_max = a * n_append
        for offset in range(len(a)):
            if b == a_max[offset: offset + len(b)]:
                return ceil((offset + len(b)) / len(a))

        return -1

        """

        if len(b) == 0:
            return 0

        if len(a) == 0:
            return -1

        n_append = ceil(len(b) / len(a))
        a_max = a * n_append
        if b in a_max:
            return n_append

        # We could implement speed up here, as we don't need to check for match at places where we already did above.
        elif b in a * (n_append + 1):
            return n_append + 1

        else:
            return -1


assert Solution().repeatedStringMatch( "abcd","cdabcdab") == 3
assert Solution().repeatedStringMatch( "a","aa") == 2
