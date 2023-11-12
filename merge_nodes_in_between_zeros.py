# Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/
from typing import Optional

from utils import ListNode


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Input is the head (the first node) of the linked list.
        It contains series of integers seperated by 0s.
        The list has 0 at the beginning and 0 at the end.

        For every 2 consecutive 0s, merge all nodes in between into a single node summing them into single merge node.
        The modified list is witout 0s.
        Return the modified list.


        # Examples

        >>> ListNode.to_list(Solution().mergeNodes(ListNode.from_list([0, 3, 1, 0, 4, 5, 2, 0])))
        [4, 11]

        >>> ListNode.to_list(Solution().mergeNodes(ListNode.from_list([0, 1, 0, 3, 0, 2, 2, 0])))
        [1, 3, 4]

        >>> ListNode.to_list(Solution().mergeNodes(ListNode.from_list([0])))
        []

        >>> ListNode.to_list(Solution().mergeNodes(ListNode.from_list([0, 1, 0])))
        [1]


        # Compare Extreme Approaches to Get to The Correct Answer

        This is simple summation at the first look.
        One just needs to keep reference to the first node of the interval enclosed by zeros.
        Then accumulate the sum until reaching another zero.
        Then just connecting the first node to the next node of the second zero and update the number to the sum.
        The complexity is O(N).


        # Risk
        The last node has no next value.
        The initial values are not correctly initialized.

        """

        if head is None or head.next is None:
            return None

        node = head
        while True:
            z = node
            node = z.next
            while node.val != 0:
                z.val += node.val
                node = node.next

            if node.next is None:
                z.next = None
                return head

            z.next = node
