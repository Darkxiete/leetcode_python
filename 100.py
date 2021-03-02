from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_dfs_iterative3
from typing import List


class Solution:
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:
        """
        recursive
        :param p:
        :param q:
        :return:
        """
        if p and q:
            return p.val == q.val and self.isSameTree1(p.left, q.left) and self.isSameTree1(p.right, q.right)
        return p is q

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        iterative - my version
        :param p:
        :param q:
        :return:
        """
        if p and q:
            stack = []
            while p and q or stack:
                while p and q:
                    stack.append((p, q))
                    p = p.left
                    q = q.left
                # 如果p q 不同时为None则False
                if (p or q) and None in (p, q):
                    return False
                p, q = stack.pop()
                if not p or not q:
                    return False
                if p.val != q.val:
                    return False
                p = p.right
                q = q.right
            return True
        else:
            return p is q

    def isSameTree3(self, p: TreeNode, q: TreeNode) -> bool:
        """
        iterative BFS
        :param p:
        :param q:
        :return:
        """
        queue = [(p, q)]
        while queue:
            p, q = queue.pop(0)
            if not p and not q:
                continue
            elif None in (p, q):
                return False
            else:
                if p.val != q.val:
                    return False
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True


if __name__ == '__main__':
    n1 = [1, None, 2]
    n2 = [1, 2]
    bt1 = create_btree(n1)
    bt2 = create_btree(n2)
    s = Solution()
    print(s.isSameTree3(bt1, bt2))
