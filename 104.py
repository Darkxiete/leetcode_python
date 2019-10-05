from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level
from typing import List


class Solution:
    def maxDepth1(self, root: TreeNode) -> int:
        """
        iterative
        :param root:
        :return:
        """
        if not root:
            return 0
        level, queue, height = [], [root], 1
        while queue:
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                height += 1
            queue = level[:]
            level = []
        return height

    def maxDepth2(self, root: TreeNode) -> int:
        """
        recursive
        假设每个叶子节点的高度都是0，从叶子节点网上逐层+1得到父节点的高度
        :param root:
        :return:
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth2(root.left), self.maxDepth2(root.right))


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    bt = create_btree(nums)
    s = Solution()
    print(s.maxDepth2(bt))
