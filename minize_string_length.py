## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        """
        Given a string `s`.
        Operation: select position `i` with character `c`, delete closest occurent of `c` to the left if any and right if any.
        Repeat Operation any number of times to minimize length of string `s`.
        Return length of the minimized string.

        The operation above, allows us to deduplicate characters in the string.
        While removing the middle duplicates lead to faster results, because we can remove the characters in pairs.

        >>> Solution().minimizedStringLength("aikadua")
        5

        # Explanation: I would select the middle "a" to remove. len("ikadu")


        >>> Solution().minimizedStringLength("aaabc")
        3

        # len("abc")


        >>> Solution().minimizedStringLength("cbbd")
        3


        >>> Solution().minimizedStringLength("dddaaa")
        2

        # len("abc")


        Another opportunity is ability to find the duplicate characters quickly.
        Perhaps one option would be to index them with for example dictionary.

        Let me index the string into dictionary by character.
        Then deduplicate within that index.
        Then return remaining length.

        Now to save time, I can just use set to get the right answer already and get the same result.

        """

        # char_index = defaultdict(list)
        # for i, c in enumerate(s):
        #    char_index[c].append(i)
        # for c in char_index:
        #   indexes = char_index[c]
        #   indexes.pop(0); indexes.pop(-1)
        #
        # ...

        return len(set(s))