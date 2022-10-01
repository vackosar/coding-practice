class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


def list_to_nodes(arr: list):
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

