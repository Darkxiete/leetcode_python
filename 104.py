from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # TODO
        depth = 0
        queue = [root]
        while queue:
            root = queue.pop(0)
            if not queue:
                depth += 1
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return depth


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7, 1]
    bt = create_btree(nums)
    show_btree_dfs_iterative3(bt)
    s = Solution()
    print("====")
    print(s.maxDepth(bt))
