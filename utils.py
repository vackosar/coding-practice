from collections import deque
from numbers import Number
from typing import List, Optional


class ListNode:
    def __init__(self, val: Number = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(arr: list):
        if len(arr) == 0:
            return None

        else:
            head = ListNode(arr[0], None)
            node = head
            for n in arr[1:]:
                new_node = ListNode(n, None)
                node.next = new_node
                node = new_node

            return head

    @staticmethod
    def to_list(node: 'ListNode') -> list:
        """
        >>> ListNode.to_list(ListNode.from_list([1,2,3]))
        [1, 2, 3]
        """

        if node is None:
            return []

        else:
            result = []
            while node is not None:
                result.append(node.val)
                node = node.next

            return result

    def __repr__(self):
        return f'({self.val}, {self.next})'

    def __eq__(self, other):
        return isinstance(other, ListNode) and self.to_list(self) == self.to_list(other)

    def __hash__(self):
        return hash(tuple(self.to_list(self)))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_level_order_list(input_list: List[int]):
        l = list(input_list)
        # assert l[-1] is not None
        root = TreeNode(l.pop(0))
        last_level = [root]
        while True:
            current_level = []
            for i in last_level:
                if len(l) == 0:
                    return root

                pop = TreeNode(l.pop(0))
                if pop.val is not None:
                    current_level.append(pop)
                    i.left = pop

                if len(l) == 0:
                    return root

                pop = TreeNode(l.pop(0))
                if pop.val is not None:
                    current_level.append(pop)
                    i.right = pop

                if len(l) == 0:
                    return root

            last_level = current_level

    def to_level_order_list(self):
        # Empty list to store the node values
        result = []

        # Create a deque for BFS
        q = deque()
        q.append(self)

        while q:
            # Dequeue an item from queue
            node = q.popleft()

            if node is None:
                result.append(None)
                continue

            result.append(node.val)

            # Enqueue left child
            if node.left is not None:
                q.append(node.left)
            else:
                q.append(None)

            # Enqueue right child
            if node.right is not None:
                q.append(node.right)
            else:
                q.append(None)

        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()

        return result


class ListNodeDoublyLinked:

    def __init__(self, key, value, prev_node: Optional['ListNodeDoublyLinked'], next_node: Optional[
        'ListNodeDoublyLinked']):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return f'({self.key}: {self.value})'


class NAryTreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

    @staticmethod
    def from_list(arr: list) -> 'NAryTreeNode':
        """
        (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the None value.)

        >>> NAryTreeNode.from_list([1, None, 3, 2, 4, None, 5, 6])
        NAryTreeNode(1, [NAryTreeNode(3, [NAryTreeNode(5, []), NAryTreeNode(6, [])]), NAryTreeNode(2, []), NAryTreeNode(4, [])])

        >>> NAryTreeNode.from_list([1,None,2,None,3,4,None,5,None,6])
        NAryTreeNode(1, [NAryTreeNode(2, [NAryTreeNode(3, [NAryTreeNode(5, [])]), NAryTreeNode(4, [NAryTreeNode(6, [])])])])

        >>> NAryTreeNode.from_list([1,None,2,3,4,5,None,None,6])
        NAryTreeNode(1, [NAryTreeNode(2, []), NAryTreeNode(3, [NAryTreeNode(6, [])]), NAryTreeNode(4, []), NAryTreeNode(5, [])])

        """

        if not arr:
            return None

        if len(arr) == 1:
            return NAryTreeNode(arr[0], [])


        it = iter(arr)
        root_val = next(it)
        root = NAryTreeNode(root_val)
        queue = [root]
        next(it)  # Skip None.

        while queue:
            current = queue.pop(0)
            for child_val in it:
                if child_val is None:
                    break
                child = NAryTreeNode(child_val)
                current.children.append(child)
                queue.append(child)

        return root


    def __repr__(self):
        return f"NAryTreeNode({self.val}, {self.children.__repr__()})"

    def to_list(self) -> list:
        """
        >>> NAryTreeNode.to_list(NAryTreeNode(1, [NAryTreeNode(3, [NAryTreeNode(5, []), NAryTreeNode(6, [])]), NAryTreeNode(2, []), NAryTreeNode(4, [])]))
        [1, None, 3, 2, 4, None, 5, 6]

        >>> NAryTreeNode.to_list(NAryTreeNode(1, [NAryTreeNode(2, [NAryTreeNode(3, [NAryTreeNode(5, [])]), NAryTreeNode(4, [NAryTreeNode(6, [])])])]))
        [1, None, 2, None, 3, 4, None, 5, None, 6]

        >>> NAryTreeNode(1, [NAryTreeNode(2, []), NAryTreeNode(3, [NAryTreeNode(6, [])]), NAryTreeNode(4, []), NAryTreeNode(5, [])]).to_list()
        [1, None, 2, 3, 4, 5, None, None, 6]
        """

        result = []
        queue = deque([self])
        result.append(self.val)
        result.append(None)  # Separator.

        while queue:
            node = queue.popleft()
            for child in node.children:
                result.append(child.val)
                queue.append(child)

            result.append(None)  # Separator.

        # Removing the trailing `None`.
        while result and result[-1] is None:
            result.pop()

        return result


def call_with_inputs(obj, methods, values, expecteds):
    skip_check = False
    if expecteds is None:
        expecteds = [None] * len(methods)
        skip_check = True

    assert len(methods) == len(values) == len(expecteds)
    for method, value, expected in zip(methods, values, expecteds):
        actual = getattr(obj, method)(*value)
        if not skip_check:
            assert expected == actual, f"{method}(*{value}) == {actual} != {expected}"


assert TreeNode.from_level_order_list([1, 3, None, None, 2]).to_level_order_list() == [1, 3, None, None, 2]
# trailing values are ignored
assert TreeNode.from_level_order_list([1, None, None]).to_level_order_list() == [1]
assert TreeNode.from_level_order_list([1]).to_level_order_list() == [1]
assert  TreeNode.from_level_order_list([3, 9, 20, None, None, 15, 7]).to_level_order_list() == [3, 9, 20, None, None, 15, 7]