from typing import List, Union


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while any(lists):
            m = 2 << 31
            j = 0
            for i in range(len(lists)):
                if lists[i] and m > lists[i].val:
                    j = i
                    m = lists[j].val
            curr.next = lists[j]
            curr = curr.next
            lists[j] = lists[j].next

        return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> Union[ListNode, None]:
        def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(None)
            curr = dummy
            c1 = l1
            c2 = l2
            while c1 and c2:
                if c1.val < c2.val:
                    curr.next = c1
                    c1 = c1.next
                else:
                    curr.next = c2
                    c2 = c2.next
                curr = curr.next
            if c1:
                curr.next = c1
            if c2:
                curr.next = c2
            return dummy.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        head = merge_two_list(lists[0], lists[1])
        for i in range(2, len(lists)):
            head = merge_two_list(head, lists[i])
        return head

    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        def merge(lists: List[ListNode], left: int, right: int):
            if left == right:
                return lists[left]
            if left + 1 == right:
                return merge_two_list(lists[left], lists[right])
            mid = (left + right) // 2
            l = merge(lists, left, mid)
            r = merge(lists, mid + 1, right)
            return merge_two_list(l, r)

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            return merge(lists, 0, len(lists) - 1)


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


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    return dummy.next


if __name__ == '__main__':
    s = Solution()
    for f in [s.mergeKLists1, s.mergeKLists2, s.mergeKLists3]:
        a = create_listnode([1, 4, 5])
        b = create_listnode([1, 3, 4])
        c = create_listnode([2, 6])
        show_listnode(f([a, b, c]))
