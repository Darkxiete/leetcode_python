from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        d = ListNode(0)
        c = d
        c1 = l1
        c2 = l2
        while c1 and c2:
            if c1.val <= c2.val:
                c.next = c1
                c = c.next
                c1 = c1.next
            else:
                c.next = c2
                c = c.next
                c2 = c2.next
        c.next = c1 if c1 else c2
        return d.next


def create_listnode(nums: List[int]) -> ListNode:
    head = curr = ListNode(nums[0])
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head


def show_listnode(head: ListNode) -> None:
    curr = head
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print('\n')


if __name__ == '__main__':
    s = Solution()
    ln1 = create_listnode([1, 2, 3])
    ln2 = create_listnode([6])
    show_listnode(ln1)
    show_listnode(ln2)
    ans = s.mergeTwoLists(ln1, ln2)
    show_listnode(ans)
