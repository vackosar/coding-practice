class Solution(object):
    def wordPattern(self, pattern, s):
        """
        String pattern is a list of characters. String s is a list of words.
        Find if words follow the pattern of the characters. The same characters need to match the same words.

        Expect that the characters may not always be alphabetical "abcdef".
        Iteratively map words to their characters.
        Then compare the two lists.

        The solution is O(N).

        :type pattern: str
        :type s: str
        :rtype: bool
        """


        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        char_map = []
        for c in pattern:
            if c not in char_map:
                char_map.append(c)

        chars_code = 0
        word_chars = ""
        word_to_char = dict()
        for word in s.split(" "):
            word_char = word_to_char.get(word)
            if word_char is None:
                if chars_code == len(char_map):
                    return False

                word_char = char_map[chars_code]
                chars_code += 1
                word_to_char[word] = word_char

            word_chars += word_char

        return word_chars == pattern


assert not Solution().wordPattern(pattern ="abba", s ="dog cat cat fish")
assert Solution().wordPattern(pattern="e", s="eukera")
assert Solution().wordPattern("abba", "dog cat cat dog")
assert not Solution().wordPattern("abba", "dog cat dog cat")