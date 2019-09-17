from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree
from typing import List


class Solution:
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        level, ans = [], []
        while queue:
            level = queue[:]
            tmp = []
            for node in level:
                tmp.append(node.val)
            ans.append(tmp)
            queue = []
            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans[::-1]

    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        """
        recursive
        :param root:
        :return:
        """

        def dfs(root, level, res):
            if root:
                if len(res) < level + 1:
                    res.insert(0, [])  # O(N)
                res[-(level + 1)].append(root.val)
                dfs(root.left, level + 1, res)
                dfs(root.right, level + 1, res)

        res = []
        dfs(root, 0, res)
        return res

    def levelOrderBottom3(self, root: TreeNode) -> List[List[int]]:
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue
                     if node for child in (node.left, node.right)]
        return res[-2::-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 9, 20, None, None, 15, 7]
    bt = create_btree(nums)
    print(s.levelOrderBottom3(bt))
