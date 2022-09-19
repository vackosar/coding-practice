from typing import Optional, List

from utils import call_with_inputs

english_chars = 'abcdefghijklmnopqrstuvwxyz'


class CharNode:
    """
    https://leetcode.com/problems/implement-magic-dictionary/
    
    Search a dictionary and return true if you find a word with same length and exactly one character different. Return false otherwise.
    """

    def __init__(self, char: Optional[str]):
        if char is not None:
            assert len(char) == 1
            assert char in english_chars
            self.char = char

        else:
            self.char = None

        self.char_children: list[Optional[CharNode]] = [None] * len(english_chars)
        self.is_final = False

    def insert(self, word: str):
        if len(word) == 0:
            self.is_final = True

        else:
            char = word[0:1]
            subword = word[1:]
            index = english_chars.index(char)
            if self.char_children[index] is None:
                self.char_children[index] = CharNode(char)

            self.char_children[index].insert(subword)

    def search(self, word: str, remaining_edits: int):
        if len(word) == 0:
            return self.is_final and remaining_edits == 0

        else:
            char = word[0:1]
            subword = word[1:]
            index = english_chars.index(char)

            if self.char_children[index] is not None and self.char_children[index].search(subword, remaining_edits):
                return True

            if remaining_edits > 0:
                for index, char_child in enumerate(self.char_children):
                    if char_child is not None and char_child.char != char:
                        result = char_child.search(subword, remaining_edits - 1)
                        if result:
                            return True

            return False


class MagicDictionary:

    def __init__(self):
        self.node = CharNode(None)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.node.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.node.search(searchWord, 1)

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

md = MagicDictionary()
md.buildDict(["hello", "leetcode"])


call_with_inputs(md, ["search", "search", "search"],
                 [["hhllo"], ["hell"], ["leetcoded"]],
                 [True, False, False])

call_with_inputs(md, ["search", "search", "search", "search"],
    [["hello"], ["hhllo"], ["hell"], ["leetcoded"]],
    [False, True, False, False])
