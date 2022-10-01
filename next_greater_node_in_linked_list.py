from typing import Optional, List

from utils import list_to_nodes, ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
        Return array where for each node there is a next bigger value following the nodes position.


        # Brute force
        On each step iterate over entire array looking for nodes that are zero, and setting a bigger value.

        # Set
        Keep a set of nodes with their indexes, for which we are yet to find bigger value.
        Once found set to result array once.


        """

        result = []
        to_find = []

        i = 0
        while head is not None:

            # Check and set if head contains bigger value. Need to run over a copy not the original set.
            # Search here would be faster if the to_find set was sorted. Now it can be as much as N.
            last_smaller_find_index = -1
            for f_i, (j, val) in enumerate(to_find):
                if head.val > val:
                    # Found the first next bigger value.
                    result[j] = head.val
                    last_smaller_find_index = f_i

                else:
                    # head.val <= val
                    break

            # Append the current value keeping to_find array sorted.
            to_find = [(i, head.val)] + to_find[last_smaller_find_index + 1:]

            # Next.
            i += 1
            head = head.next
            result.append(0)

        return result


assert Solution().nextLargerNodes(list_to_nodes([2, 7, 4, 3, 5])) == [7, 0, 5, 5, 0]
assert Solution().nextLargerNodes(list_to_nodes([9, 7, 6, 7, 6, 9])) == [0, 9, 7, 9, 9, 0]
