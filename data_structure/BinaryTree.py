from typing import List


class BinaryTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_btree(nums):
    def _create_btree(root, i, n, nums: List[int]) -> BinaryTree:
        """
        Initialize a complete Binary Tree
        :param top:
        :param index:
        :param nums:
        :return:
        """
        if i < n:
            root = BinaryTree(nums[i])
            root.left = _create_btree(root.left, 2 * i + 1, n, nums)
            root.right = _create_btree(root.right, 2 * i + 2, n, nums)
        return root
    root = BinaryTree(0)
    return _create_btree(root, 0, len(nums), nums)


def show_btree_recursive1(root):
    """
    pre-order
    :param root:
    :return:
    """
    if root:
        print(root.val, end='\t')
        show_btree_recursive1(root.left)
        show_btree_recursive1(root.right)


def show_btree_recursive2(root):
    """
    in-order
    :param root:
    :return:
    """
    if root:
        show_btree_recursive2(root.left)
        print(root.val, end='\t')
        show_btree_recursive2(root.right)


def show_btree_recursive3(root):
    """

    :param root:
    :return:
    """
    if root:
        show_btree_recursive3(root.left)
        show_btree_recursive3(root.right)
        print(root.val, end='\t')


def show_btree_iterative1(root):
    """
    level
    :param root:
    :return:
    """


def show_btree_iterative2(root):
    """
    pre-order
    :param root:
    :return:
    """
    stack = []
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def show_btree_iterative3(root):
    """
    pre-order
    :param root:
    :return:
    """

    def visit_along_left_branch(node, stack):
        while node:
            print(node.val)
            stack.append(node.right)
            node = node.left

    stack = []
    while True:
        visit_along_left_branch(root, stack)
        if not stack:
            break
        root = stack.pop()


def show_btree_iterative4(root):
    """
    in-order
    :param root:
    :return:
    """

    def go_along_left_branch(node, stack):
        while node:
            stack.append(node)
            node = node.left

    stack = []
    while True:
        go_along_left_branch(root, stack)
        if not stack:
            break
        root = stack.pop()
        print(root.val)
        root = root.right


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, None, 2, 3]
    bt = create_btree(nums1)
    show_btree_iterative1(bt)
