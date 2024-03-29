from bisect import bisect_left
from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        """
        # Problem Description
        Phrases is list of phrases. Phrase is lowercase string or english letters and spaces. No space at the start or the end. No consecutive spaces.

        Return Before and After puzzles, which are phrases that are mergers of two phrases where last word of first phrase is the same as the first word of the second phrase. Return all possible puzzles of all different pairs of phrases. Return in sorted lexicographically.


        # Examples Including Edge Cases
        >>> Solution().beforeAndAfterPuzzles(["a b", "c d", "b a"])
        ['a b a', 'b a b']

        >>> Solution().beforeAndAfterPuzzles(["a b", "c d"])
        []

        >>> Solution().beforeAndAfterPuzzles(["c d", "x c", "b y", "a b"])
        ['a b y', 'x c d']

        >>> Solution().beforeAndAfterPuzzles(["writing code", "code rocks"])
        ['writing code rocks']

        >>> Solution().beforeAndAfterPuzzles(["a","b","a"])
        ['a']


        # Reasoning about Solution Approaches To Find The Best One

        Brute force solution would be N**2 time.
        The core problem here is efficient search, which we could do with a hash maps.
        The hash map will cost O(N) memory but can reduce computation to O(N).
        Returning in sorted order requires additional sort of O(N Log N).


        # The Solution Implementation:
        """

        first = dict()

        for i, phrase in enumerate(phrases):
            words = phrase.split(' ')
            # assert len(words) > 1
            first_word = words[0]
            if first_word not in first:
                first[first_word] = []

            first[first_word].append((i, phrase))

        # We can use both set or sorted list. Sorted list should be a bit faster.
        results = []
        # results = set()
        for i, prefix_phrase in enumerate(phrases):
            prefix_phrase_words = prefix_phrase.split(' ')
            last = prefix_phrase_words[-1]
            prefix_short = ' '.join(prefix_phrase_words[:-1])

            suffix_list = first.get(last)
            if suffix_list is not None:
                for suffix_phrase_i, suffix_phrase in suffix_list:
                    # prevent the duplicate
                    if i != suffix_phrase_i:
                        # results.add((prefix_short + " " + suffix_phrase).strip())
                        s = (prefix_short + " " + suffix_phrase).strip()
                        lo = bisect_left(results, s, lo=0, hi=None)
                        if lo == len(results) or results[lo] != s:
                            results.insert(lo, s)

        # return list(sorted(results))
        return results
