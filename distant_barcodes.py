from collections import Counter
from typing import List


# FIXME NOT DONE


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        The barcodes is a list of integer numbers.
        Rearrange the numbers so that no two adjacent numberes are equal.
        Return the solution, which is guaranteed to exist.


        # Examples

        # >>> check([51,83,51,40,51,40,51,40,83,40,83,83,51,40,40,51,51,51,40,40,40,83,51,51,40,51,51,40,40,51,51,40,51,51,51,40,83,40,40,83,51,51,51,40,40,40,51,51,83,83,40,51,51,40,40,40,51,40,83,40,83,40,83,40,51,51,40,51,51,51,51,40,51,83,51,83,51,51,40,51,40,51,40,51,40,40,51,51,51,40,51,83,51,51,51,40,51,51,40,40])
        # None

        # In this case, we have to be careful about not being left with some last numbers 8. We have to be able to distribute them in.
        >>> check([7, 7, 7, 8, 5, 7, 5, 5, 5, 8])
        [7, 5, 8, 7, 5, 8, 7, 5, 7, 5]

        # This is a simple case.
        >>> check([1, 1, 2, 2])
        [1, 2, 1, 2]

        # Many 1s Example
        # In this case, we have to make sure that all 1s are separated.
        >>> check([1, 1, 1, 1, 2, 2, 3, 3])
        [1, 2, 1, 2, 1, 3, 1, 3]

        # This case is complicated for the right order. We have to start with the most common number first.
        >>> check([2, 1, 1])
        [1, 2, 1]


        # Approaches

        It is not possible to do this if there is more than halve of one identical number in the array.
        Otherwise we can simply always be odd-even mixing two different numbers next to each other.

        Brute force would be on each new number to iterate across others and try to find non equal.
        Faster is use some sort or bucketing.

        The sort itself with odd from start and even from the end won't work,
        because if we have suffient number of items in the middle this strategy will fail.
        For example [1, 1, 2, 2, 2, 3, 3, 3] ->  [1, 3, 1, 3, 2, 3, 2, 2]

        So instead we need bucketing with counting.
        Count all numbers, then iteratively mix two different buckets, until non are left.
        This will be O(N) time and O(N) space.

        Simple iteration over the buckets is not enough, because when
        ```
        counter = Counter(barcodes)
        keys = list(counter.keys())

        assert len(keys) > 1
        first_i = 0

        solution = []
        while True:
            if len(solution) > 0 and solution[-1] == keys[first_i]:
                solution.insert(0, keys[first_i])
                assert len(solution) == len(barcodes)
                return solution

            solution.append(keys[first_i])
            counter[keys[first_i]] -= 1

            if len(solution) == len(barcodes):
                return solution

            while True:
                first_i += 1
                if first_i == len(keys):
                    first_i = 0

                if counter[keys[first_i]] > 0:
                    break
        ```


        # Risks

        Not using all the numbers.
        The two indexes could conflict in various way. They must not use the same counter, they must not overflow.
        FIXME The two indexes seems like a wrong idea. What if I instead iterated across all at all times?

        """

        if len(barcodes) == 1:
            return barcodes

        counter = Counter(barcodes)
        keys = [key for key, value in sorted(counter.items(), key=lambda item: item[1], reverse=True)]
        # keys = list(counter.keys())

        assert len(keys) > 1
        first_i = 0
        second_i = 1

        solution = []
        while True:
            solution.append(keys[first_i])
            counter[keys[first_i]] -= 1

            if len(solution) == len(barcodes):
                return solution

            if counter[keys[first_i]] == 0:
                first_i += 1
                while first_i < len(keys) and (first_i == second_i or counter[keys[first_i]] == 0):
                    first_i += 1

                # prevent inserting the last 1 or 2 numbers next to each other
                if first_i > len(keys) - 1:
                    insert_i = 0
                    while len(solution) < len(barcodes):
                        solution.insert(insert_i, keys[first_i])
                        insert_i += 2

                    assert len(solution) == len(barcodes)
                    return solution

            solution.append(keys[second_i])
            counter[keys[second_i]] -= 1

            if len(solution) == len(barcodes):
                return solution

            if counter[keys[second_i]] == 0:
                second_i += 1
                while second_i < len(keys) and (first_i == second_i or counter[keys[second_i]] == 0):
                    second_i += 1

                # prevent inserting the last 1 or 2 numbers next to each other
                if second_i > len(keys) - 1:
                    insert_i = 0
                    while len(solution) < len(barcodes):
                        solution.insert(insert_i, keys[first_i])
                        insert_i += 2

                    assert len(solution) == len(barcodes)
                    return solution


def check(barcodes: List[int]):
    solution = Solution().rearrangeBarcodes(barcodes)
    assert list(sorted(solution)) == list(sorted(barcodes))
    previous = None
    for n in solution:
        if previous is not None:
            assert n != previous

        previous = n

    return solution



