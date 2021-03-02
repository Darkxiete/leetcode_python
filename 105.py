from DataStructure.BinaryTree import BinaryTree as TreeNode, create_btree, show_btree_bfs_iterative_with_level
from typing import List


class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        # index of root node
        in_end_index = inorder.index(root.val)
        len_left_tree = in_end_index
        root.left = self.buildTree1(preorder[1: len_left_tree + 1], inorder[0: len_left_tree])
        root.right = self.buildTree1(preorder[len_left_tree + 1:], inorder[len_left_tree + 1:])
        return root

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree2(preorder, inorder[0: index])
            root.right = self.buildTree2(preorder, inorder[index + 1:])
            return root

    def buildTree3(self, preorder, inorder):
        """
        Iterative
        preorder: N L R
        inorder: L N R
        不管前序还是中序遍历都需要先递归左子树，达到最左下的节点，当前序到达最左下节点时，前序节点=中序节点
        因此开始发生回溯，沿着之前的路径往回回溯，此时前序index-1（以下代码通过pop实现），中序index+1
        直到中序节点！=前序节点，此时中序开始遍历右子树
        因此前序遍历的下一个节点应该是“前序中序公共最高节点”的右子树的根节点，
        “前序中序公共最高节点”可以通过循环`while stack and stack[-1].val == inorder[ino]`来检查
        每找一次“前序中序公共最高节点”，中序索引就往后一位，并且需要记录该公共节点，下面代码中使用的是`prev`指针
        当找到“前序中序公共最高节点”，开遍历右子树
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder:
            return None

        root = TreeNode(preorder.pop(0))
        stack = [root]

        ino = 0
        while preorder:
            curr = TreeNode(preorder.pop(0))
            prev = None
            while stack and stack[-1].val == inorder[ino]:
                prev = stack.pop()
                ino += 1
            if prev:
                prev.right = curr
            else:
                stack[-1].left = curr

            stack.append(curr)
            # pre += 1
            # print('-----')
            # show_btree_bfs_iterative_with_level(root)
            # print('-----')
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    input1 = ([1, 2, 4, 8, 9, 5, 3, 6, 7], [8, 4, 9, 2, 5, 1, 6, 3, 7])
    input2 = ([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 6, 3])
    s = Solution()
    # show_btree_bfs_iterative_with_level(s.buildTree3(preorder, inorder))
    show_btree_bfs_iterative_with_level(s.buildTree3(*input2))
