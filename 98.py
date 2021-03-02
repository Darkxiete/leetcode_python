from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List


class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        """
        递归
        ~~左树存在一个上界，右树存在一个下界~~
        每个节点都存在一个上下界
        空间复杂度：O(lgn)~O(n)
        时间复杂度：O(n)
        :param root:
        :return:
        """

        def _isValidBST(root, minNode, maxNode):
            if not root:
                return True
            if minNode and root.val <= minNode.val or maxNode and root.val >= maxNode.val:
                return False
            return _isValidBST(root.left, minNode, root) and _isValidBST(root.right, root, maxNode)

        return _isValidBST(root, None, None)

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        中序遍历，如果非严格递增则return False
        空间复杂度：O(n)
        时间复杂度：O(n)
        :param root:
        :return:
        """
        if not root:
            return True
        stack = []
        ans = []
        while True:
            while root is not None:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
                if ans and root.val <= ans[-1]:
                    return False
                ans.append(root.val)
                root = root.right
            else:
                break
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [3, 3]
    bt = create_btree(nums)
    show_btree_dfs_iterative3(bt)
    print(s.isValidBST2(bt))
