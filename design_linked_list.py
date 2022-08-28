from typing import Optional

from utils import call_with_inputs


class Node:
    def __init__(self, val: int, prev_node: Optional['Node'], next_node: Optional['Node']):
        self.prev_node = prev_node
        self.next_node = next_node
        self.val = val

    def __repr__(self):
        return str(self.__dict__)


class MyLinkedList:
    """
    https://leetcode.com/problems/design-linked-list/submissions/
    Design linked list, which ignores inputs with invalid indexes.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, index: int) -> int:
        if index >= self.count or index < 0:
            return -1

        node = self.get_node_at_index(index)
        if node is None:
            return -1

        else:
            return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        if self.tail is not None:
            new_tail = Node(val, self.tail, None)
            self.tail.next_node = new_tail
            self.tail = new_tail

        else:
            self.tail = Node(val, None, None)

        if self.head is None:
            self.head = self.tail

        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return

        elif index == self.count:
            self.addAtTail(val)
            return

        node = self.get_node_at_index(index)
        assert node is not None

        prev_node = node.prev_node
        new_node = Node(val, prev_node, node)
        node.prev_node = new_node

        if prev_node is not None:
            prev_node.next_node = new_node

        else:
            self.head = new_node

        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return

        # if index == 0 and self.count == 1:
        #     self.head = None
        #     self.tail = None

        node = self.get_node_at_index(index)
        prev_node = node.prev_node
        next_node = node.next_node
        if prev_node is not None:
            prev_node.next_node = next_node

        else:
            self.head = next_node

        if next_node is not None:
            next_node.prev_node = prev_node

        else:
            self.tail = prev_node

        self.count -= 1

    def get_node_at_index(self, index: int):
        if index >= self.count:
            return None

        node = self.head
        for j in range(index + 1):
            if node is None:
                if j == index:
                    return None

                else:
                    raise ValueError(f"Unexpected list end at {j} in {self}!")

            elif j == index:
                return node

            else:
                node = node.next_node

        return None


call_with_inputs(MyLinkedList(),
                 ["addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
                 [[1], [3], [1, 2], [1], [1], [1]],
                 [None, None, None, 2, None, 3]
                 )

call_with_inputs(
    MyLinkedList(),
    ["addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead", "addAtTail", "get", "addAtHead",
     "addAtIndex", "addAtHead"],
    [[7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]],
    [None, None, None, None, None, None, None, 4, None, None, None]
)

