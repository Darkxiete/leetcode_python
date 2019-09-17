from data_structure.ListNode import ListNode, create_listnode, show_listnode
from typing import List


class Solution:
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        """
        recursive
        :param head:
        :param k:
        :return:
        """
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup1(curr, k)
            while count > 0:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -= 1
            head = curr
        return head

    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        count = 0
        prev = dummy = ListNode(0)
        curr = tail = dummy.next = head
        while curr and curr.next:
            count += 1
            curr = curr.next
            if count == k - 1:
                while count > 0:
                    tmp = tail.next.next
                    tail.next.next = prev.next
                    prev.next = tail.next
                    tail.next = tmp
                    count -= 1
                prev = tail
                tail = tail.next
                curr = tail
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    ln = create_listnode(nums)
    show_listnode(s.reverseKGroup2(ln, 1))
    ln = create_listnode(nums)
    show_listnode(s.reverseKGroup2(ln, 2))
    ln = create_listnode(nums)
    show_listnode(s.reverseKGroup2(ln, 3))  #
    ln = create_listnode(nums)
    show_listnode(s.reverseKGroup2(ln, 4))
    ln = create_listnode(nums)
    show_listnode(s.reverseKGroup2(ln, 5))
