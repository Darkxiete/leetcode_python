from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level
from typing import List


class Solution:
    def isBalanced1(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            left_height = depth(root.left)
            right_height = depth(root.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        return depth(root) != -1

    def isBalanced2(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return True
        left_height = depth(root.left)
        right_height = depth(root.right)
        return abs(left_height - right_height) <= 1 and self.isBalanced2(root.left) and self.isBalanced2(root.right)


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    bt = create_btree(nums)
    s = Solution()
    print(s.isBalanced1(bt))
