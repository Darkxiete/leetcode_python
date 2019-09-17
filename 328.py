from listnode.ListNode import ListNode, create_listnode, show_listnode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pe = po = dummy = ListNode(0)
        curr = dummy.next = head
        first_even_node = None
        count = 1
        while curr:
            if count % 2 == 1:
                po.next = curr
                po = po.next
            else:
                if not first_even_node:
                    first_even_node = curr
                    pe = curr
                else:
                    pe.next = curr
                    pe = pe.next
            curr = curr.next
            count += 1

        po.next = first_even_node
        pe.next = None
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    ln = create_listnode(nums)
    show_listnode(ln)

    ans = s.oddEvenList(ln)
    show_listnode(ans)
