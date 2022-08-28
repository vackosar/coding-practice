from typing import Optional

from utils import call_with_inputs


class ListNode:

    def __init__(self, key, value, prev_node: Optional['ListNode'], next_node: Optional['ListNode']):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return f'({self.key}: {self.value})'


class LRUCache:
    """
    https://leetcode.com/problems/lru-cache/
    
    For O(1) access using a key a hash map is used.
    A doubly linked list is used to keep the access recency ordering, because it has complexity of O(1) for operations of remove from head, append to tail, and remove middle item.

    Remember that least recently used simply reorders on each access, so no usage statistics counting is needed!
    Remember that LRU cache only fills up to full capacity and only then starts to forget!
    Remember that moving an item of doubly linked list requires operation modification of both left and right neighbors!
    """

    def __init__(self, capacity: int):
        assert capacity > 0
        self.capacity = capacity
        self.dic = dict()
        # will we pop from here
        self.head = None
        # will append here
        self.tail = None

    def put(self, key, value):
        node = self.dic.get(key)
        if node is not None:
            self.move_to_tail(node)
            node.value = value
            return

        else:
            if self.capacity == 0:
                # pop from head
                self.dic.pop(self.head.key)
                self.remove(self.head)

            else:
                self.capacity -= 1

            new_node = ListNode(key, value, None, None)
            self.append(new_node)
            self.dic[key] = new_node

    def move_to_tail(self, node: ListNode):
        if node is self.tail:
            return

        self.remove(node)
        self.append(node)

    def append(self, node: ListNode):
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        node.prev_node = self.tail
        self.tail.next_node = node
        self.tail = node

    def remove(self, node: ListNode):
        if self.head is node:
            self.head = node.next_node

        if self.tail is node:
            self.tail = node.prev_node

        if node.prev_node is not None:
            node.prev_node.next_node = node.next_node

        if node.next_node is not None:
            node.next_node.prev_node = node.prev_node

        node.next_node = None
        node.prev_node = None

    def get(self, key) -> int:
        node = self.dic.get(key)
        if node is None:
            return -1

        else:
            self.move_to_tail(node)
            return node.value


call_with_inputs(LRUCache(10),
                 ["put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
                  "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get",
                  "put", "get", "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put",
                  "put", "get", "put", "put", "put", "put", "get", "put", "put", "get", "put", "put", "get", "put",
                  "put", "put", "put", "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get",
                  "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get", "put",
                  "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get", "get", "get", "put",
                  "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"],
                 [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22],
                  [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1],
                  [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12],
                  [3, 27], [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12],
                  [10], [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9],
                  [6], [3, 4], [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26],
                  [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1],
                  [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24],
                  [9, 26], [13, 28], [11, 26]], None)

call_with_inputs(
    LRUCache(3),
    ["put", "put", "put", "put", "get", "get", "get", "get", "put", "get", "get", "get", "get", "get"],
    [[1, 1], [2, 2], [3, 3], [4, 4], [4], [3], [2], [1], [5, 5], [1], [2], [3], [4], [5]],
    [None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5]
)

call_with_inputs(LRUCache(2), ["put", "put", "get", "put", "get", "put", "get", "get", "get"],
                 [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
                 [None, None, 1, None, -1, None, -1, 3, 4]
                 )

call_with_inputs(LRUCache(1), ["put", "get", "put", "get", "get"], [[2, 1], [2], [3, 2], [2], [3]], [None, 1, None, -1, 2])
