from data_structure.BinaryTree import Node


class Solution:
    def connect(self, root: Node) -> Node:
        """
        对于可能存在空节点的点，可以用哨兵节点的技巧
        :param root:
        :return:
        """
        dummy = Node(0, 0, 0, root)
        head = tail = Node(0, 0, 0, 0)
        while root:
            for node in (root.left, root.right):
                tail.next = node
                if node:
                    tail = tail.next
            if root.next:
                root = root.next
            else:
                root, tail = head.next, head
        return dummy.next
