from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level, \
    stringToTreeNode
from typing import List


class Solution:
    def hasPathSum1(self, root: TreeNode, Sum: int) -> bool:
        """
        recursive
        :param root:
        :param Sum:
        :return:
        """
        if not root:
            return False
        if root.left is None and root.right is None and root.val == Sum:
            return True
        return self.hasPathSum1(root.left, Sum - root.val) or self.hasPathSum1(root.right, Sum - root.val)

    def hasPathSum2(self, root: TreeNode, Sum: int) -> bool:
        """
        dfs with stack
        :param root:
        :param Sum:
        :return:
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == Sum:
                    return True
            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))
        return False

    def hasPathSum3(self, root: TreeNode, Sum: int) -> bool:
        """
        dfs with queue
        :param root:
        :param Sum:
        :return:
        """
        # TODO


if __name__ == '__main__':
    inputs = [
        ("[5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, null, null, 1]", 22),
        ("[1,null,2,null,3,null,4,null,5]", 15)
    ]
    i = 1
    nums = inputs[i][0]
    Sum = inputs[i][1]
    s = Solution()
    bt = stringToTreeNode(nums)

    show_btree_bfs_iterative_with_level(bt)
    print(s.hasPathSum2(bt, Sum))
