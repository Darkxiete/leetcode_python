from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level
from typing import List


class Solution:
    def minDepth1(self, root: TreeNode) -> int:
        """
        recursive
        要注意一种特殊情况
              0
            1   2
              3   4
                 5
        以上二叉树，节点4的高度是2而不是1，高度只能从叶子结点开始计算
        :param root:
        :return:
        """
        if not root:
            return 0
        left = self.minDepth1(root.left)
        right = self.minDepth1(root.right)
        return 1 + min(left, right) if left and right else left + right + 1

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, level = [root], []
        height = 0
        while queue:
            height += 1
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                if not node.left and not node.right:
                    return height
            queue = level[:]
            level = []
        return height


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    bt = create_btree(nums)
    s = Solution()
    print(s.minDepth2(bt))
