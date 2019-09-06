from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def reverse1(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy.next
    p = curr.next
    curr.next = None
    while p:
        curr = p
        p = curr.next
        curr.next = dummy.next
        dummy.next = curr
    return dummy.next


def reverse2(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    curr = head
    prev = None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev


def reverse3(head: ListNode) -> ListNode:
    prev = None
    while head:
        _next = head.next
        head.next = prev
        prev = head
        head = _next
    return prev


def reverse4(head: ListNode) -> ListNode:
    """
    递归版本
    :param head:
    :return:
    """
    if head.next is None:
        return head
    new_head = reverse3(head.next)
    head.next.next = head
    head.next = None
    return new_head


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    """
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
    :param head:
    :param m:
    :param n:
    :return:
    """
    count = 1
    p = head
    while count < m:
        p = p.next
        count += 1
    start = p
    while p.next and count < n:
        q = p.next
        q.next = p
        start.next = q.next
        p = q
        count += 1
        head.next = q
    return head


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    ln = create_listnode(nums)
    show_listnode(ln)
    ln = reverse3(ln)
    show_listnode(ln)
