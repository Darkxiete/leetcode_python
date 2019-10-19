from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level, \
    stringToTreeNode
from typing import List


class Solution:
    def __init__(self):
        self.maxPath = -2 ** 31

    def maxPathSum1(self, root: TreeNode) -> int:
        """
        前序遍历，每次计算一颗子树(或子节点)的maxPath，
        :param root:
        :return:
        """

        def dfs(root):
            if not root:
                return 0
            l = max(0, dfs(root.left))  # 小于0的就不取了
            r = max(0, dfs(root.right))
            self.maxPath = max(self.maxPath, l + r + root.val)
            return root.val + max(l, r)

        dfs(root)
        return self.maxPath

    def maxPathSum2(self, root: TreeNode) -> int:
        """
        前序遍历，之后倒过来，就是一种从最底层开始的遍历序列
        计算子树的numPath时需要从底层子树开始
        :param root:
        :return:
        """
        def presort(root):
            if not root:
                return root
            stack = [root]
            res = []
            while stack:
                curr = stack.pop()
                res.append(curr)
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            return res

        ans = -2 ** 31
        node_dict = {None: 0}
        for node in presort(root)[::-1]:
            left = max(node_dict.get(node.left), 0)
            right = max(node_dict.get(node.right), 0)
            node_dict[node] = max(left, right) + node.val
            ans = max(left + right + node.val, ans)
        return ans


if __name__ == '__main__':
    nums = "[2,-1]"
    bt = stringToTreeNode(nums)
    show_btree_bfs_iterative_with_level(bt)
    s = Solution()
    print(s.maxPathSum2(bt))
