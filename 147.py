from listnode.ListNode import ListNode, create_listnode, show_listnode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        curr = dummy.next = head
        while curr and curr.next:
            val = curr.next.val
            if curr.val <= val:
                curr = curr.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val <= val:
                p = p.next
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = p.next   # 不是 tmp.next = curr   e.g. [4, 4, 3, 2, 1]
            p.next = tmp
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 1]
    list_node = create_listnode(nums)
    show_listnode(list_node)
    ans = s.insertionSortList(list_node)
    show_listnode(ans)
