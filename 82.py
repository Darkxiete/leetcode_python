from data_structure.ListNode import ListNode, create_listnode, show_listnode
from typing import Union


class Solution:
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        """
        额外链表
        :param head:
        :return:
        """
        dummy = ListNode(0)
        curr = dummy.next = head
        h = l = ListNode(0)

        while curr and curr.next:
            if curr.val != curr.next.val:
                l.next = curr
                curr = curr.next
                l = l.next
            else:
                tmp = curr.val
                while curr and curr.val == tmp:
                    curr = curr.next
        l.next = curr
        return h.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        """
        in-place
        :param head:
        :return:
        """
        pre = dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next

    def deleteDuplicates3(self, head: ListNode) -> ListNode:
        """
        recursive
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates3(head.next)
        else:
            head.next = self.deleteDuplicates3(head.next)
        return head

    def deleteDuplicates4(self, head: ListNode) -> ListNode:
        """
        backtrack
        :param head:
        :return:
        """

        def backtrack(head: ListNode, pre: Union[ListNode, None]) -> Union[ListNode, None]:
            if not head:
                return head
            if pre and pre.val == head.val or head.next and head.val == head.next.val:
                return backtrack(head.next, head)
            else:
                head.next = backtrack(head.next, head)
                return head

        return backtrack(head, None)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 3, 4, 4]
    ln = create_listnode(nums)
    show_listnode(ln)
    ans = s.deleteDuplicates2(ln)
    show_listnode(ans)
