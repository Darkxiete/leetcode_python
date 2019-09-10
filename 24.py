from utils.ListNode import *
from typing import List


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        fast = head.next
        slow = head
        n = 0
        while fast:
            if n % 2 == 0:
                slow.val, fast.val = fast.val, slow.val
            fast = fast.next
            slow = slow.next
            n += 1
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    a = create_listnode([])
    show_listnode(s.swapPairs(a))

