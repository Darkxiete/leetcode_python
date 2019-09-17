from data_structure.ListNode import ListNode, create_listnode, show_listnode


class Solution:
    """
    思路
    1. 使用栈，然后从后面开始计算和，计算一个生成一个节点
    2. 计算两个列表的数值，然后算和，然后逐个生成节点
    3. 递归 TODO
    """
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        无法应对N位进位 比如
        333, 667
        :param l1:
        :param l2:
        :return:
        """
        def add(p1, c1, p2, c2):
            curr = dummy = ListNode(None)
            while c1 > c2:
                curr.next = p1
                curr = curr.next
                p1 = p1.next
                c1 -= 1
            while p1 and p2:
                v = p1.val + p2.val
                if v >= 10:
                    if curr.val:
                        curr.val += 1
                    else:
                        curr.next = ListNode(1)
                        curr = curr.next
                    v -= 10
                curr.next = ListNode(v)
                curr = curr.next
                p1 = p1.next
                p2 = p2.next
            return dummy.next

        curr = l1
        count1 = 0
        while curr:
            curr = curr.next
            count1 += 1
        curr = l2
        count2 = 0
        while curr:
            curr = curr.next
            count2 += 1

        if count1 > count2:
            ans = add(l1, count1, l2, count2)
        else:
            ans = add(l2, count2, l1, count1)
        return ans

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用栈
        :param l1:
        :param l2:
        :return:
        """
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next

        s = 0
        tail = ListNode(0)
        while stack1 or stack2:
            if stack1:
                s += stack1.pop().val
            if stack2:
                s += stack2.pop().val
            tail.val = int(s % 10)
            tmp = ListNode(int(s // 10))
            tmp.next = tail
            tail = tmp
            s /= 10
        return tail if tail.val != 0 else tail.next


if __name__ == '__main__':
    """
    正常  9, 0
    进一位 1, 9
    进两位 22, 78
    进N位 3334, 6666
    """
    s = Solution()

    nums1 = [2, 2]
    nums2 = [7, 8]
    ln1 = create_listnode(nums1)
    ln2 = create_listnode(nums2)
    show_listnode(ln1)
    show_listnode(ln2)
    show_listnode(s.addTwoNumbers2(ln1, ln2))
