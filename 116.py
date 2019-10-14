from data_structure.BinaryTree import Node


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0, 0, 0, root)
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return dummy.next
