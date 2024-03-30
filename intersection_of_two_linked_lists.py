from typing import Optional

from utils import ListNode


## Follow Vaclav Kosar for more software and machine learning at https://vaclavkosar.com/


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Return intersection node of the linked lists.

        That is a first node where `a.next = b.next`.


        # Examples

        >>> c  = ListNode(1)
        >>> a  = ListNode(0, c)
        >>> b  = ListNode(3, c)
        >>> Solution().getIntersectionNode(a, b) == c
        True

        >>> a  = ListNode(0, ListNode(3, None))
        >>> b  = ListNode(3, ListNode(4, None))
        >>> Solution().getIntersectionNode(a, b) == None
        True

        # Solution

        Since without remembering, I will not know the intersection when it occurs.
        The simplest solution is to remember all nodes from one hash-set for O(N) memory.
        And then find the first intersection where for O(N).

        Alternative could perhaps involve some suffix array?
        Interesting how many problems are about asking which datastructure is the best.


        # Avoid Problems

        Avoid problems when on the first or last node and make sure that it will proceed correctly.


        # Solution
        """

        if not headA or not headB:
            return None

        nodes_a = set()
        current_node_a = headA
        nodes_a.add(current_node_a)
        while current_node_a:
            nodes_a.add(current_node_a)
            current_node_a = current_node_a.next

        current_node_b = headB
        while current_node_b:
            if current_node_b in nodes_a:
                return current_node_b

            current_node_b = current_node_b.next