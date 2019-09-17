from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree
from typing import List


class Solution:
    """
    3
   / \
  9  20
    /  \
   15   7
    [
      [3],
      [9,20],
      [15,7]
    ]
    """

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, level, queue = [], [], []
        queue.append(root)
        ans.append([root.val])
        while queue or level:
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level[:]
            tmp = []
            for t in level:
                if t.val is not None:
                    tmp.append(t.val)
            if tmp:
                ans.append(tmp)
            level = []
        return ans

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        def helper(res, root, height):
            if not root:
                return
            if height >= len(res):
                res.append([])
            res[height].append(root.val)
            helper(res, root.left, height + 1)
            helper(res, root.right, height + 1)
        res = []
        helper(res, root, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-8, 3, 0, -8, None, None, None, None, -1, None, 8]
    bt = create_btree(nums)
    print(s.levelOrder2(bt))
