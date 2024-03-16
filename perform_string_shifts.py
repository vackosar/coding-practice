from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/



class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """
        Input is a string `s` lowercase letter and matrix `shift`.
        `shift[i] = [direction[i], amount[i]]`

        direction can be 0 for left shift and 1 for right shift.
        amount is the shift size.
        left shift by 1 means moving first character in `s` to the end of `s`.

        Return string after all operations.


        # Examples

        shifts: abc -> bca -> cab
        >>> Solution().stringShift("abc", [[0, 1], [1, 2]])
        'cab'

        >>> Solution().stringShift("wpdhhcj", [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]])
        'hcjwpdh'

        >>> Solution().stringShift("abcdefg", [])
        'abcdefg'


        # Reasoning To Get To The Correct Answer

        Iterate throught the shifts and apply them.
        Simplest shift is just one character at a time.


        # Invent Better Alternative Solution

        Sum up the shift first, and then apply resulting operation.

        # Mistakes To Avoid

        Don't forget to use absolute value for the negatives.
        Don't forget to concatenate strings correctly.


        # Estimate Complexity Cost

        O(N), O(1)

        """

        if len(s) == 0:
            return s

        total_shift = 0
        for direction, amount in shift:
            if direction == 0:
                total_shift -= amount

            else:
                total_shift += amount

        if total_shift == 0:
            return s

        elif total_shift < 0:

            for i in range(-total_shift):
                s = s[1:] + s[0]

            return s

        elif total_shift > 0:
            for i in range(total_shift):
                s = s[-1] + s[:-1]

            return s
