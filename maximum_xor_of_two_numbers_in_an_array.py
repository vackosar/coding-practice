from typing import List


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        # Problem Description

        You are given non-empty positive integer array `nums`.
        Return maximum of nums[i] XOR nums[j], where 0 <= i <= j < n.

        XOR is a bit-wise or logical operation, that is the same as OR except for input (1, 1):


        # Examples Including Edge Cases

        >>> 0 ^ 0
        0

        >>> 1 ^ 0
        1

        >>> 0 ^ 1
        1

        >>> 1 ^ 1
        0

        1 = 01
        2 = 10
        3 = 11
        >>> 2 ^ 1
        3

        >>> 3 ^ 0
        3


        1 = 0001
        5 = 0101
        >>> 5 ^ 1
        4

        5 = 0101
        >>> 5 ^ 5
        0

        1 = 0001
        8 = 1000
        >>> 8 ^ 1
        9

        From above, we can see that XOR can also lead to decrease of the larger value.

        So to get the biggest value, we want the highest bit 1, and then the others if possible too.
        That brings us to the examples:

        1 = 0001
        5 = 0101
        8 = 1000
        >>> Solution().findMaximumXOR([1, 5, 8])
        13

        1 = 0001
        5 = 0101
        5 = 0101
        >>> Solution().findMaximumXOR([1, 5, 5])
        4

        >>> Solution().findMaximumXOR([3,10,5,25,2,8])
        28


        # Reasoning about Solution Approaches To Find The Best One

        Brute force would be N**2 in time.

        Faster solution ideally involves some sort of sorted search or backtracking.
        We want to preserve the highest order bits, but sometimes we have no choice and may have to focus on the lower bits.

        We could always start trying to combine one top-bit number with the next highest bit numbers, which always will be bigger than combining 2 highest order bit numbers.
        If there are no lower bit numbers, only then we would select some other higher order bit. We would pop the highest bit and perform the indentical decision on that level.
        This recursion would lead to a solution of around N*logN speed.
        For this we would need to sort the numbers into buckets by their highest bits. We can find the highest bit with log2 function, but we would like full decomposition.
        So either there is some function for this or we need to iterative divide by 2.


        ## Experimental Pseudo-Code Implementation 1:

        ```
        def convert_to_bit_string(n: int) -> str:
            # TODO implement
            pass

        high_bit_to_string = dict()
        for n in nums:
            s = convert_to_bit_string(n)
            if len(s) not in high_bit_to_string:
                high_bit_to_string[len(s)] = []

            high_bit_to_string[len(s)].append(s)

        max_bits = list(sorted(list(high_bit_to_string), reverse=True))
        max_bit = max_bits[-1]
        for s in high_bit_to_string[max_bit]:
            # next_max_bit depends on the next highest bit of the number
            for s2 in high_bit_to_string[max_bit]

        ```

        Ok, above is close, because it focuses on the bits and should iterate somewhere around in N * log(N).
        A problem there is in that it is not clearly explained what happens if we don't have XOR-1 for the highest bit.
        Searching twice first in the high-bit-1 numbers and then high-bit-0 numbers or both. In fact we have to merge these into single list.
        We can merge then if we discart the top bit after we find out if we can XOR-1 not there, and then continue looking at the lower bits,
        while making sure that we only look at numbers that fit the pattern of the top-bit.
        Here below is a simpler solution for this better idea.

        We will need to use additional condition that is true to help us find the solution: `c = a ^ b` then `assert (a ^ c == b) and (b ^ c == a)`.

        >>> 5 ^ 7
        2

        >>> 5 ^ 7 ^ 5
        7

        >>> 5 ^ 7 ^ 7
        5



        In our case, we the `c` is the answer, and the condition tells us that the answer
        We can take advantage of a fact that iterating over bit-masks is Log(N), and the fact that we can build the answer bit-by-bit.
        Reading in the previous solution we can see that we are starting with the top bit and only need to verify if there is corresponding another number that does not have that high bit.
        If we don't find such number answer has to have a zero on that point.
        The same idea can be used iteratively:
        We would build the optimal XOR answer_prefix by searching from the left and selecting the best pairs for that prefix.
        Progressively we would filter based on the already found ideal prefix and XOR only the next bit for
        Idea is from: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/solutions/3052355/fast-python-solution-beats-99/


        # The Solution Implementation:

        """

        answer_prefix = 0
        for i in range(32)[::-1]:
            # Bit shift to longer prefix, to give place for the next bit.
            answer_prefix <<= 1
            # This extracts all prefixes of len i.
            prefixes = {num >> i for num in nums}
            # This filters for the numbers with the prefix answer_prefix and also checking that we have two ideal numbers to XOR. If not we add 0 to answer_prefix.
            prefix_with_1_on_the_lowest_bit = answer_prefix ^ 1
            # If we XOR the answer_prefix with any of the other number prefixes, we should get the other number in the XOR, which should be in the prefixes, if it is the correct one.
            # And because the prefix has 1 on the lowest bit it will tell us if that we can have 1 on that position for the maximum number, otherwise we will set 0 into the answer onto that position.
            answer_prefix += any(prefix_with_1_on_the_lowest_bit ^ p in prefixes for p in prefixes)

        # At this point we have full answer.
        return answer_prefix