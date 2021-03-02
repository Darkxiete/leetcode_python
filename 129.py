from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level, \
    stringToTreeNode
from typing import List


class Solution:
    def sumNumbers1(self, root: TreeNode) -> int:
        """
        dfs
        :param root:
        :return:
        """
        if not root:
            return 0
        stack = [(root, [root])]
        ans = 0
        while stack:
            curr, path = stack.pop(0)
            if not curr.left and not curr.right:
                sum = 0
                for node in path:
                    sum = sum * 10 + node.val
                ans += sum
            if curr.right:
                stack.append((curr.right, path + [curr.right]))
            if curr.left:
                stack.append((curr.left, path + [curr.left]))
        return ans

    def sumNumbers2(self, root: TreeNode) -> int:
        def dfs(root, path, ans):
            if not root:
                return 0
            if not root.left and not root.right:
                sum = 0
                for node in path:
                    sum = sum * 10 + node.val
                ans += sum
            if root.left:
                dfs(root.left, path + [root.left], ans)
            if root.right:
                dfs(root.right, path + [root.right], ans)

        ans = 0
        dfs(root, [root], 0)
        return ans


if __name__ == '__main__':
    nums = "[4,9,0,5,1]"
    bt = stringToTreeNode(nums)
    s = Solution()
    print(s.sumNumbers2(bt))
