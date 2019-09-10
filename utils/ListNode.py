from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_listnode(nums: List[int]):
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next


def show_listnode(ln: ListNode):
    while ln:
        print(ln.val, end='->')
        ln = ln.next
    print("\n")
