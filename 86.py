from data_structure.ListNode import ListNode, create_listnode, show_listnode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l1.next = h2.next
        l2.next = None
        return h1.next


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 3, 2, 5, 2]
    val = 3
    ln = create_listnode(nums)
    show_listnode(ln)
    ans = s.partition(ln, val)
    show_listnode(ans)