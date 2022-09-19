from typing import Optional, List

from utils import call_with_inputs


class MagicDictionary:
    """
    https://leetcode.com/problems/implement-magic-dictionary/

    Return True if there is a word in the dictionary which differs in exactly one character, not more not less. Otherwise return False.
    """

    def __init__(self):
        self.node = CharNode(None)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.node.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.node.search(searchWord, 1)


class CharNode:

    def __init__(self, char: Optional[str]):
        if char is not None:
            self.char = char

        else:
            self.char = None

        self.char_dict = dict()
        self.is_final = False

    def insert(self, word: str):
        if len(word) == 0:
            self.is_final = True

        else:
            char = word[0:1]
            subword = word[1:]
            child = self.char_dict.get(char)
            if child is None:
                child = CharNode(char)
                self.char_dict[char] = child

            child.insert(subword)

    def search(self, word: str, remaining_edits: int):
        if len(word) == 0:
            return self.is_final and remaining_edits == 0

        else:
            char = word[0:1]
            subword = word[1:]

            child = self.char_dict.get(char)
            if child is not None and child.search(subword, remaining_edits):
                return True

            if remaining_edits > 0:
                for child_char, child in self.char_dict.items():
                    if child_char != char and child.search(subword, remaining_edits - 1):
                        return True

                return False


md = MagicDictionary()
call_with_inputs(md, ["buildDict", "search", "search", "search", "search"],
                 [[["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]],
                 [None, False, True, False, False])
