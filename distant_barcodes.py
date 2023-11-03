from collections import Counter
from heapq import heappush, heappop
from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        The barcodes is a list of integer numbers.
        Rearrange the numbers so that no two adjacent numberes are equal.
        Return the solution, which is guaranteed to exist.


        # Examples Including Edge Cases

        >>> check([51,83,51,40,51,40,51,40,83,40,83,83,51,40,40,51,51,51,40,40,40,83,51,51,40,51,51,40,40,51,51,40,51,51,51,40,83,40,40,83,51,51,51,40,40,40,51,51,83,83,40,51,51,40,40,40,51,40,83,40,83,40,83,40,51,51,40,51,51,51,51,40,51,83,51,83,51,51,40,51,40,51,40,51,40,40,51,51,51,40,51,83,51,51,51,40,51,51,40,40])

        # In this case, we have to be careful about not being left with some last numbers 8. We have to be able to distribute them in.
        # Example solution: [7, 5, 8, 7, 5, 8, 7, 5, 7, 5]
        >>> check([7, 7, 7, 8, 5, 7, 5, 5, 5, 8])

        # This is a simple case.
        # Example solution [1, 2, 1, 2]
        >>> check([1, 1, 2, 2])

        # Many 1s Example
        # In this case, we have to make sure that all 1s are separated.
        # Example solution: [1, 2, 1, 2, 1, 3, 1, 3]
        >>> check([1, 1, 1, 1, 2, 2, 3, 3])


        # This case is complicated for the right order. We have to start with the most common number first.
        # Example solution: [1, 2, 1]
        >>> check([2, 1, 1])


        # Reasoning about Radical Solution Approaches To Find The Best One Of The Correct

        It is not possible to do this if there is more than half of one identical number in the array.
        Otherwise, we can simply always be odd-even mixing two different numbers next to each other.

        Brute force would be on each new number to iterate across others and try to find non-equal.
        Faster is use some sort or bucketing.

        The sort itself with odd from start and even from the end won't work,
        because if we have suffient number of items in the middle this strategy will fail.
        For example [1, 1, 2, 2, 2, 3, 3, 3] ->  [1, 3, 1, 3, 2, 3, 2, 2]

        So instead we need bucketing with counting.
        Count all numbers, then iteratively mix two different buckets, until non are left.
        This will be O(N) time and O(N) space.

        A round-robin iteration over the buckets in a round  is not enough, because if we have a number that is there many times, it fill fail:

        Another approach is to have 2 indexes that are the most common and mix those.
        The two indexes is wrong idea, because if you don't prioritize the most common numbers,
        you are not solving the problem recursively and the rules that you expect stop holding.
        In this case you may be using less common numbers first, and end up with some numbers left without ability to mix them.
        You could remix ditribute them back to the existing result, because those were not used at the beginning, but it is complex.

        The correct approach is to make sure we are using up the most common numbers at all times.
        We can do that with keeping sort with a heap.
        We mix them in even-odd making sure we never append the same numbers.

        Inspiration: https://leetcode.com/problems/distant-barcodes/solutions/2497111/82-tc-easy-python-solution/


        # Risks

        Not using all the numbers.
        The two indexes could conflict in various way. They must not use the same counter, they must not overflow.
        Pushing back to sorted heap too early, making impossible to find the second most common number.
        """

        # Count the numbers into a counter dictionary.
        counter = Counter(barcodes)
        heap = []
        for i in counter:
            # insert sorted from the highest count to the lowest
            heappush(heap, (-counter[i], i))

        result = []
        previously_appended_result_number = -1
        while heap:
            # Get the currently most common number.
            negative_count_1, number_1 = heappop(heap)

            # Check if we pushed this the most common number just previously.
            if previously_appended_result_number != number_1:

                # Append to the result and remember the last number.
                result.append(number_1)
                previously_appended_result_number = number_1

                # If there is count left, sort it back to the sorted heap.
                if negative_count_1 + 1:
                    heappush(heap, (negative_count_1 + 1, number_1))

            else:
                # Get the second most common number instead.
                negative_count_2, number_2 = heappop(heap)

                # Append to the result and remember the last number.
                result.append(number_2)
                previously_appended_result_number = number_2

                # If there is count left, sort it back to the sorted heap.
                if negative_count_2 + 1:
                    heappush(heap, (negative_count_2 + 1, number_2))

                # Return the most common number back to sorted heap, making it the most common again.
                heappush(heap, (negative_count_1, number_1))

        return result


def check(barcodes: List[int]):
    solution = Solution().rearrangeBarcodes(barcodes)
    assert list(sorted(solution)) == list(sorted(barcodes))
    previous = None
    for n in solution:
        if previous is not None:
            assert n != previous

        previous = n

    return None



