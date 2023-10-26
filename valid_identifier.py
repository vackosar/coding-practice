import re

RESERVED_WORDS = {"Python", "Cobra", "Anaconda"}

validation = re.compile(r'[a-zA-Z_][_a-zA-Z0-9]*')


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def isValidIdentifier(self, identifier: str) -> bool:
        """
        Given a string, determine if it's a valid identifier.

        Here are the rules for a valid identifier:

            An identifier must start with a letter (a-z, A-Z) or underscore (_).

            The rest of the identifier can contain letters, underscores (_) and digits (0-9).

            An identifier cannot be a reserved word. For simplicity, let's say the only reserved words are "Python", "Cobra", and "Anaconda".

        Your function should return true if the string is a valid identifier and false otherwise.

        >>> Solution().isValidIdentifier("a123")
        True

        >>> Solution().isValidIdentifier("123a")
        False

        >>> Solution().isValidIdentifier("_python")
        True

        >>> Solution().isValidIdentifier("Python")
        False

        >>> Solution().isValidIdentifier("Cobra")
        False

        >>> Solution().isValidIdentifier("a123***")
        False

        >>> Solution().isValidIdentifier("*a123")
        False

        """
        # Check if the identifier is a reserved word
        if identifier in RESERVED_WORDS:
            return False

        return validation.fullmatch(identifier) is not None



solutions = [
    ("_" + "Python" * 20, True),
 ("1234567890"*1000000, False),
 ("a"*100 + "1234567890"*999, True),
 ("1Cobra"*200000, False),
 ("*Anaconda"*200000, False),
 ("_"*100 + "1234567890"*9999, True),
 ("a"*1000000 + "_"*999999, True),
 ("_" + "Python"*200000, True),
 ("abcde"*1000000 + "1234567890"*999999, True)]


import concurrent.futures
import time

def execute_solution(solution):
    identifier, expected_result = solution
    start_time = time.perf_counter()
    result = Solution().isValidIdentifier(identifier)
    end_time = time.perf_counter()
    assert result == expected_result, f"For identifier {identifier}, expected {expected_result} but got {result}"
    return end_time - start_time

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    times = executor.map(execute_solution, solutions)

for i, solution, execution_time in zip(range(len(solutions)), solutions, times):
    print(f"Execution time for solution {i} was {execution_time} seconds")

