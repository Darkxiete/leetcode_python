from listnode.ListNode import ListNode, create_listnode, show_listnode


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        def getSize(head):
            counter = 0
            while head is not None:
                counter += 1
                head = head.next
            return counter

        def split(head, step):
            """
            前进 step 步 然后cut一下， 这样head就是一个长度为step的ListNode
            返回一个从head开始的第 step 个Node
            :param head:
            :param step:
            :return:
            """
            i = 1
            while i < step and head:
                head = head.next
                i += 1

            if head is None:
                return None
            # disconnect/cut
            temp, head.next = head.next, None
            return temp

        def merge(l, r, head):
            """
            将两个ListNode合并
            以 head 为头，往后将l r merge的结果填上，然后返回最后一个Node的位置
            :param l:
            :param r:
            :param head:
            :return:
            """
            cur = head
            while l and r:
                if l.val < r.val:
                    cur.next, l = l, l.next
                else:
                    cur.next, r = r, r.next
                cur = cur.next

            cur.next = l if l is not None else r
            # 让cur指向最后一个Node
            while cur.next is not None:
                cur = cur.next
            return cur

        size = getSize(head)
        bs = 1
        dummy = ListNode(0)
        dummy.next = head
        while bs < size:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 3, 2, 4, 5, 6]
    ln = create_listnode(nums)
    show_listnode(ln)
    ans = s.sortList(ln)
    show_listnode(ans)
