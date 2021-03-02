from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List, Union


class Solution:
    def generateTrees1(self, n: int) -> List[TreeNode]:
        """
        递归法
        :param n:
        :return:
        """
        def _generateTrees(start: int, end: int) -> List[Union[TreeNode, None]]:
            ans = []
            if start > end:
                ans.append(None)
                return ans
            for i in range(start, end + 1):
                left = _generateTrees(start, i - 1)
                right = _generateTrees(i + 1, end)
                for ln in left:
                    for rn in right:
                        root = TreeNode(i)
                        root.left = ln
                        root.right = rn
                        ans.append(root)
            return ans

        return _generateTrees(1, n) if n != 0 else []

    def generateTrees2(self, n: int) -> List[TreeNode]:
        """
        递归改dp
        :param n:
        :return:
        """
        def clone(root: TreeNode, offset: int) -> Union[TreeNode, None]:
            if not root:
                return None
            node = TreeNode(root.val + offset)
            node.left = clone(root.left, offset)
            node.right = clone(root.right, offset)
            return node

        dp = [[] for _ in range(n + 1)]
        if n == 0:
            return dp[0]
        dp[0].append(None)
        for length in range(1, n + 1):
            for root_len in range(1, length + 1):
                left = root_len - 1
                right = length - root_len
                for left_tree in dp[left]:
                    for right_tree in dp[right]:
                        root = TreeNode(root_len)
                        root.left = left_tree
                        root.right = clone(right_tree, root_len)
                        dp[length].append(root)
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    n = 10
    ans = s.generateTrees2(n)
    print(len(ans))
    for a in ans:
        show_btree_dfs_iterative3(a)
        print('---')
