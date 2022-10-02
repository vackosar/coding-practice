# Definition for singly-linked list.
from typing import Optional

from utils import ListNode


# https://leetcode.com/problems/add-two-numbers/solution/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 2 linked lists, non-neg integers, non-empty . reverse order, each single digit encoded.
        # Add and return sum as linked list. No leading zeros, except for zero integer.
        # I should be able to just use summation with carry

        start_node = ListNode(None, None)
        cnode = start_node
        carry = 0

        while True:
            csum = carry
            if l1 is not None:
                l1_next = l1.next
                csum += l1.val

            else:
                l1_next = None

            if l2 is not None:
                l2_next = l2.next
                csum += l2.val

            else:
                l2_next = None

            cnode.val = csum % 10
            carry = csum // 10

            if carry != 0 or l1_next is not None or l2_next is not None:
                l1 = l1_next
                l2 = l2_next
                new_node = ListNode(None, None)
                cnode.next = new_node
                cnode = new_node

            else:
                break

        return start_node


# [2,4,3], -> [7,0,8]