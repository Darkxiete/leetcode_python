from DataStructure.ListNode import create_listnode, show_listnode


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Input: 1->2->3->4->5->NULL, m = 2, n = 4
        Output: 1->4->3->2->5->NULL
        :param head:
        :param m:
        :param n:
        :return:
        """
        if not head or m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for i in range(m - 1):
            p = p.next
        tail = p.next
        for i in range(n - m):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    ln = create_listnode(nums)
    show_listnode(ln)

    s = Solution()
    ln = s.reverseBetween(ln, 1, 5)
    show_listnode(ln)
