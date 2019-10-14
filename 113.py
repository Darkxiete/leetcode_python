from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level, \
    stringToTreeNode
from typing import List


class Solution:
    """
            5
         / \
        4   8
       /   / \
      11  13  4
     /  \    / \
    7    2  5   1
    sum = 22
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
    Summary:
    这类题考得就是二叉树的遍历，只不过在遍历的同时需要保存每个节点的和，可以用，因此自然而然的可以想用用dfs来做
    需要注意的是：
        遍历的时候使用
        ```
        while root:
            stack.append(...)
            root = root.left
        ```
        这种遍历方法并不太好，因为无法获得上一次压栈的值，也就无法很好的保存已访问过的节点以及目前节点的和
    """

    def pathSum1(self, root: TreeNode, Sum: int) -> List[List[int]]:
        """
        dfs-recursive
        :param root:
        :param Sum:
        :return:
        """

        def dfs(root, Sum, path, ans):
            if not root.left and not root.right and Sum == root.val:
                path.append(root.val)
                ans.append(path)
            if root.left:
                dfs(root.left, Sum - root.val, path + [root.val], ans)
            if root.right:
                dfs(root.right, Sum - root.val, path + [root.val], ans)

        if not root:
            return []
        ans = []
        dfs(root, Sum, [], ans)
        return ans

    def pathSum2(self, root: TreeNode, Sum: int) -> List[List[int]]:
        """
        dfs+stack iterative

        迭代版本其实就是自己用一个`stack`实现递归中的栈帧
        :param root:
        :param Sum:
        :return:
        """
        if not root:
            return []
        res = []
        stack = [(root, Sum - root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val - curr.right.val, ls + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, val - curr.left.val, ls + [curr.left.val]))
        return res

    def pathSum3(self, root: TreeNode, Sum: int) -> List[List[int]]:
        """
        dfs+stack iterative
        :param root:
        :param Sum:
        :return:
        """
        if not root:
            return []
        ans = []
        stack = [(root, [root.val])]
        while stack:
            curr, path = stack.pop()
            if not curr.left and not curr.right and sum(path) == Sum:
                ans.append(path)
            if curr.right:
                stack.append((curr.right, path + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, path + [curr.left.val]))
        return ans

    def pathSum4(self, root: TreeNode, Sum: int) -> List[List[int]]:
        """
        bfs+queue iterative
        :param root:
        :param Sum:
        :return:
        """
        if not root:
            return []
        queue = [(root, Sum - root.val, [root.val])]
        ans = []
        while queue:
            curr, val, path = queue.pop(0)
            if not curr.left and not curr.right and val == 0:
                ans.append(path)
            if curr.left:
                queue.append((curr.left, val - curr.left.val, path + [curr.left.val]))
            if curr.right:
                queue.append((curr.right, val - curr.right.val, path + [curr.right.val]))
        return ans


if __name__ == '__main__':
    nums = "[5,4,8,11,null,13,4,7,2,null,null,5,1]"
    s = Solution()
    bt = stringToTreeNode(nums)
    show_btree_bfs_iterative_with_level(bt)
    print(s.pathSum3(bt, 22))
