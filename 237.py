from data_structure.ListNode import ListNode, create_listnode, show_listnode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = dummy = ListNode(0)
        curr = dummy.next = head
        while curr != node:
            curr = curr.next
            prev = prev.next
        prev.next = curr.next
        return dummy.next