from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        prev = first = second = None
        if not root:
            return
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 主要逻辑
            if prev is not None and root.val <= prev.val:
                if first is None:
                    first = prev
                second = root
            prev = root
            root = root.right
        tmp = first.val
        first.val = second.val
        second.val = tmp


if __name__ == '__main__':
    s = Solution()
    nums = [1, 3, None, None, 2]
    bt = create_btree(nums)
    s.recoverTree(bt)
    show_btree_dfs_iterative3(bt)
