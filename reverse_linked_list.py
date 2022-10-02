# https://leetcode.com/submissions/detail/711793950/
from typing import Optional

from utils import ListNode


class Solution:

    def reverseList(self, head):
        prev = None
        node = head

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)

    def reverse(self, head, previous):
        if head is None:
            return previous

        elif head.next is None:
            head.next = previous
            return head

        else:
            reversed_head = self.reverse(head.next, head)
            head.next = previous
            return reversed_head