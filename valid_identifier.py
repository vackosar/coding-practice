'''

Given a string, determine if it's a valid identifier.

Here are the rules for a valid identifier:

    An identifier must start with a letter (a-z, A-Z) or underscore (_).

    The rest of the identifier can contain letters, underscores (_) and digits (0-9).

    An identifier cannot be a reserved word. For simplicity, let's say the only reserved words are "Python", "Cobra", and "Anaconda".

Your function should return true if the string is a valid identifier and false otherwise.

Input: "a123"
Output: True

Input: "123a"
Output: False

Input: "_python"
Output: True

Input: "Python"
Output: False

'''


import re

validation = re.compile(r'[a-zA-Z_][_a-zA-Z0-9]*')


class Solution:
    def isValidIdentifier(self, identifier: str) -> bool:
        """

        >>> Solution().isValidIdentifier("a123")
        True

        >>> Solution().isValidIdentifier("123a")
        False

        >>> Solution().isValidIdentifier("_python")
        True

        >>> Solution().isValidIdentifier("Python")
        True
        """
        return validation.fullmatch(identifier) is not None




