from listnode.ListNode import ListNode, create_listnode, show_listnode
from typing import List


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        while head:
            res.append(head.val)
            head = head.next
        for i in range(len(res) - 1, -1, -1):
            while stack and stack[-1] <= res[i]:
                stack.pop()
            tmp = res[i]
            res[i] = stack[-1] if stack else 0
            stack.append(tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 5]
    ln = create_listnode(nums)
    print(s.nextLargerNodes(ln))