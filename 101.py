from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List


class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        """
        iterative
        :param root:
        :return:
        """
        p = q = root
        stack = []
        while p and q or stack:
            while p and q:
                stack.append((p, q))
                p = p.left
                q = q.right
            if not p and not q:
                p, q = stack.pop()
                if p.val != q.val:
                    return False
                p = p.right
                q = q.left
            else:
                return False
        return True

    def isSymmetric2(self, root: TreeNode) -> bool:
        def is_reverse(a, b):
            if not a or not b:
                return not a and not b
            return a.val == b.val and is_reverse(a.left, b.right) and is_reverse(a.right, b.left)

        if not root:
            return True
        return is_reverse(root.left, root.right)


if __name__ == '__main__':
    nums = []
    bt = create_btree(nums)
    s = Solution()
    print(s.isSymmetric1(bt))
