from typing import List

## Follow me for more software and machine learning at https://vaclavkosar.com/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Encode into MorseCode. Return number of unique concatenations.

        >>> Solution().uniqueMorseRepresentations(["gin","zen","gig","msg"])
        2

        >>> Solution().uniqueMorseRepresentations(["a"])
        1

        """
        a_i = int('a'.encode()[0])
        chars_to_codes = {
            bytes([a_i + char_i]).decode(): code
            for char_i, code in enumerate([".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])
        }

        encoded = set()
        for word in words:
            encoded.add(''.join([chars_to_codes[c] for c in word]))

        return len(encoded)