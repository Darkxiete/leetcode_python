from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level
from typing import List

"""
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
"""


class Solution:
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        recursive
        和 preorder-inorder 那道题差不多，只不过后续的话需要反向pop inorder，然后先生成右子树
        :param inorder:
        :param postorder:
        :return:
        """
        if inorder:
            root = TreeNode(postorder.pop())
            index = inorder.index(root.val)
            root.right = self.buildTree1(inorder[index + 1:], postorder)
            root.left = self.buildTree1(inorder[:index], postorder)
            return root

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        root = TreeNode(postorder.pop())
        stack = [root]

        ino = len(inorder) - 1

        while postorder:
            curr = TreeNode(postorder.pop())
            prev = None
            while stack and stack[-1].val == inorder[ino]:
                prev = stack.pop()
                ino -= 1
            if prev:
                prev.left = curr
            else:
                stack[-1].right = curr
            stack.append(curr)
        return root


if __name__ == '__main__':
    input0 = ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    # input1 = ([1, 2, 4, 8, 9, 5, 3, 6, 7], [8, 4, 9, 2, 5, 1, 6, 3, 7])
    # input2 = ([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 6, 3])
    s = Solution()
    show_btree_bfs_iterative_with_level(s.buildTree2(*input0))
