from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        Max number of occurrences of any substring given:
        - # unique characters less than maxLetters
        - substring lenght minSize and maxSize inclusive

        For each repeated string its shortset substring is repeated the same times or more.
        So only look at the shortest substrings.
        Count all minSize strings in a map.
        """

        counter = defaultdict(lambda: 0)
        # counter = collections.Counter()
        for i in range(len(s)):
            if i + minSize <= len(s):
                suffix = s[i:i + minSize]
                if len(set(suffix)) <= maxLetters:
                    counter[suffix] += 1

        if len(counter) == 0:
            return 0

        return max(counter.values())
