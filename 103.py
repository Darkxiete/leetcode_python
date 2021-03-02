from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        ans, level, queue = [[root.val]], [], [root]
        step = -1
        while queue:
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                ans.append([i.val for i in level[::step]])
            queue = level[:]
            level = []
            step *= -1
        return ans
