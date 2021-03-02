from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans, stack = [], []
        while True:
            while root:
                ans.append(root.val)
                stack.append(root.right)
                root = root.left
            if stack:
                root = stack.pop()
            else:
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [1, None, 2, 3]
    bt = create_btree(nums)
    print(s.preorderTraversal(bt))
