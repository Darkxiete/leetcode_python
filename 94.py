from data_structure.BinaryTree import BinaryTree as TreeNode, create_btree


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def go_along_left_branch(node, stack):
            while node:
                stack.append(node)
                node = node.left

        stack = []
        ans = []
        while True:
            go_along_left_branch(root, stack)
            if not stack:
                break
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        return ans


if __name__ == '__main__':
    nums = [1, None, 3, 2]
    bt = create_btree()