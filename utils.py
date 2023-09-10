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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_level_order_list(l: List[int]):
        l = list(l)
        assert l[-1] is not None
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