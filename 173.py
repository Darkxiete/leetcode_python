from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level, \
    stringToTreeNode
from typing import List


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.iterator = self.init(root)

    def init(self, root):
        if not root:
            return root
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            yield root.val
            root = root.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return next(self.iterator)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.iterator.hasnext()

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


if __name__ == '__main__':
    nums = "[1,2,3,4]"
    bt = stringToTreeNode(nums)
    show_btree_bfs_iterative_with_level(bt)
    biter = BSTIterator(bt)
    while True:
        try:
            print(biter.next())
        except StopIteration as e:
            break