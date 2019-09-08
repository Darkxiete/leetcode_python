from listnode.ListNode import ListNode, create_listnode, show_listnode


class Solution:
    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        prev = dummy = ListNode(None)
        curr = dummy.next = head
        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = curr
            if curr:
                curr = curr.next
        return dummy.next

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

    def removeElements3(self, head: ListNode, val: int) -> ListNode:
        """
        recursive
        :param head:
        :param val:
        :return:
        """
        if not head:
            return head
        head.next = self.removeElements2(head.next, val)
        return head if head.val != val else head.next


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    val = 2
    list_nodes = create_listnode(nums)
    show_listnode(list_nodes)

    list_nodes = s.removeElements1(list_nodes, val)
    show_listnode(list_nodes)

    list_nodes = create_listnode(nums)
    list_nodes = s.removeElements2(list_nodes, val)
    show_listnode(list_nodes)

    list_nodes = create_listnode(nums)
    list_nodes = s.removeElements3(list_nodes, val)
    show_listnode(list_nodes)
