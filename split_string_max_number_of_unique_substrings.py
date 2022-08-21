
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """
       https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

        Input is a string.
        Return the maximum number of unique splits of the string into consecutive substrings.

        The number of splits is not known.
        Each len - 1 position to split is a bit, that we are deciding.

        # Brute Force
        We could start splitting by maximum splits which is len - 1.
        Then gradually reducing that if all are not unique.
        Testing all possible split variants with given split count.

        # Backtracking
        Gradually test out the splits, but remember current substrings and backtrack if a duplicate found.
        This could be fast enough since the string is max 16 long.
        Each step is an optional split. If it finds duplicate, we try making bigger step.
        After reaching the end of the string we go back to the last split and try different option.
        If we find we made fewer splits, we don't increase the maximum.

        """

        max_unique_strings = 0

        # length also gives the number of splits
        current_strings = set()

        def split(i: int):
            nonlocal max_unique_strings, current_strings

            if len(current_strings) + (len(s) - i) <= max_unique_strings:
                # Cannot find bigger solution even if I split on each character.
                return

            for j in range(i+1, len(s) + 1):
                if s[i:j] in current_strings:
                    continue

                else:
                    current_strings.add(s[i:j])
                    if j == len(s):
                        max_unique_strings = max(len(current_strings), max_unique_strings)

                    else:
                        split(j)

                    current_strings.remove(s[i:j])

            return

        split(0)
        return max_unique_strings


assert Solution().maxUniqueSplit("ababccc") == 5

# Upvote and consider following me at https://vaclavkosar.com/