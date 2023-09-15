from typing import Optional

from utils import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Given listed list head, remove all notes with a value and return new head.

        >>> ListNode.to_list(Solution().removeElements(head=ListNode.from_list([1,1,3]), val=1))
        [3]

        >>> ListNode.to_list(Solution().removeElements(head=ListNode.from_list([2,1,1,3]), val=1))
        [2, 3]

        >>> ListNode.to_list(Solution().removeElements(head=ListNode.from_list([1,1,1,1]), val=1))
        []

        >>> ListNode.to_list(Solution().removeElements(head=ListNode.from_list([]), val=1))
        []
        """

        new_head = head
        node = head
        prev_node = None
        while node is not None:
            if node.val == val:
                if prev_node is None:
                    new_head = node.next

                else:
                    prev_node.next = node.next

            else:
                # Only update prev_node if we didn't remove the node.
                prev_node = node

            node = node.next

        return new_head