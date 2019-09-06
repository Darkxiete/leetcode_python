from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd_1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        N = 0
        while curr:
            curr = curr.next
            N += 1
        i = 0
        curr = head
        prev = dummy
        while i < N - n:
            curr = curr.next
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEnd_2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


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
    head = create_listnode([1])
    show_listnode(head)
    head = s.removeNthFromEnd_2(head, 1)
    show_listnode(head)
