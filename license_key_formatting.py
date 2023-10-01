# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        You are given a licence key string `s` consisting of alphanumeric characters, that form groups, and dash as separator.
        There are n+1 groups made of n dashes.
        Reformat the string to each group containing `k` characters, except for the first group which could have less but more than zero.
        The groups must be separated by the dashes.
        Convert all lower case letters to upper case.
        Return the reformated key.

        >>> Solution().licenseKeyFormatting("a-asdf-asdf", 4)
        'A-ASDF-ASDF'

        >>> Solution().licenseKeyFormatting("a", 1)
        'A'

        >>> Solution().licenseKeyFormatting("xxxa-xx", 3)
        'XXX-AXX'

        >>> Solution().licenseKeyFormatting("aasdfasdf", 4)
        'A-ASDF-ASDF'

        >>> Solution().licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4)
        '5F3Z-2E9W'

        >>> Solution().licenseKeyFormatting(s = "2-5g-3-J", k = 2)
        '2-5G-3J'


        We want to be merging or splitting the groups to get `k` charcter long groups.
        If we go from the back of the string, ignoring the dashes, and create k-long groups, it will give us the desired results in O(n) time and O(N) space.


        """

        s = s.replace('-', '').upper()
        # Iterating character by character is slow in Python.
        # for j, c in enumerate(reversed(s)):
        # c2 = c if j % k > 0 else '-' + c

        # We can reverse the string twice, but this is again slow.
        # result = "-".join(reversed(list(s[max(j - k, 0): j] for j in range(len(s), 0, -k))))

        # Better is to start right and go right.
        start = len(s) % k
        groups = []
        if start > 0:
            groups.append(s[0: start])

        groups.extend(s[j: j + k] for j in range(start, len(s), k))

        result = "-".join(groups)

        return result

