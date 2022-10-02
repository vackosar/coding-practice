from typing import Optional, List

from utils import ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
        Input is a linked list.
        Return an array where for each input value there is a next strictly bigger value within the list or zero.


        # Brute force
        On each step iterate over entire array looking for nodes that are zero, and setting a bigger value.
        Memory complexity O(N). Time complexity at worst O(N * N). Not parallelized.

        # Stack
        Keep a set of nodes with their indexes, for which we are yet to find bigger value in a sorted stack.
        On each new value we will compare with the items in the stack, starting from the smallest values and stopping at a first bigger value.
        Memory complexity O(N). Time complexity at worst not sure but around O(N * log N). Not parallelized.
        """

        # output
        result = []

        # A stack of the values to replace sorted from biggest to the smallest.
        to_find_stack = []

        i = 0
        while head is not None:
            # Iterate smallest to the biggest while the head contains a bigger value.
            while to_find_stack and to_find_stack[-1][1] < head.val:
                j, val = to_find_stack.pop()
                # Found the first next bigger value.
                result[j] = head.val

            # Append the current value keeping to_find_stack array sorted.
            to_find_stack.append((i, head.val))

            # Next.
            i += 1
            head = head.next
            result.append(0)

        return result


assert Solution().nextLargerNodes(ListNode.from_list([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
assert Solution().nextLargerNodes(ListNode.from_list([9, 7, 6, 7, 6, 9])) == [0, 9, 7, 9, 9, 0]

# Software, machine learning and more on various social networks at https://vaclavkosar.com/