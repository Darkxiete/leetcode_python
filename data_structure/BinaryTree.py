from typing import List


class BinaryTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(string):
    input = string.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = BinaryTree(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = BinaryTree(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = BinaryTree(rightNumber)
            nodeQueue.append(node.right)
    return root


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
            root = BinaryTree(nums[i]) if nums[i] is not None else None
            if root is not None:
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


def show_btree_dfs_iterative1(root):
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


def show_btree_dfs_iterative2(root):
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


def show_btree_dfs_iterative3(root):
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


def show_btree_dfs_iterative4(root):
    """
    in-order
    :param root:
    :return:
    """
    if not root:
        return
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            print(root.val)
            root = root.right
        else:
            break


def show_btree_dfs_iterative5(root):
    """
    post-order
    mirror
    >  modified preorder (right subtree first). Then reverse the result.
    :param root:
    :return:
    """
    if not root:
        return []
    ans, stack = [], [root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    print(ans[::-1])


def post_order_traversal_iterative(root: BinaryTree):
    if not root:
        return
    stack = []
    last = None
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack[-1]
            if node.right and last != node.right:
                root = node.right
            else:
                print(node.val)
                last = node
                stack.pop()


def show_btree_bfs_recursive1(root):
    pass


def show_btree_bfs_iterative1(root):
    """
    level order
    :param root:
    :return:
    """
    if not root:
        return
    queue = [root]
    while queue:
        root = queue.pop(0)
        print(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)


def show_btree_bfs_iterative_with_level(root):
    if not root:
        return root
    level, queue = [], [root]
    print([root.val])
    while any(queue):
        for node in queue:
            if node and node.left:
                level.append(node.left)
            else:
                level.append(None)
            if node and node.right:
                level.append(node.right)
            else:
                level.append(None)
        if any(level):
            print([i.val if i else None for i in level])
        queue = level[:]
        level = []


def prev_order_traversal_morris(root: BinaryTree):
    if not root:
        return
    curr = root
    while curr:
        prev = curr.left
        if prev:
            while prev.right and prev.right != curr:
                prev = prev.right
            if not prev.right:
                prev.right = curr
                print(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
        else:
            print(curr.val)
            curr = curr.right


def in_order_traversal_morris(root: BinaryTree):
    if not root:
        return
    curr = root
    while curr:
        prev = curr.left
        if prev:
            while prev.right and prev.right != curr:
                prev = prev.right
            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                print(curr.val)  # 和pre-order的唯一不同点
                curr = curr.right
        else:
            print(curr.val)
            curr = curr.right


def post_order_traversal_morris(root: BinaryTree):
    def reverseNodes(start: BinaryTree, end: BinaryTree):
        if start == end:
            return
        x, y, z = start, start.right, None
        while x != end:
            z = y.right
            y.right = x
            x = y
            y = z

    def reverseDealNodes(start, end):
        reverseNodes(start, end)
        node = end
        while True:
            print(node.val)
            if node == start:
                break
            node = node.right
        reverseNodes(end, start)

    dummy = BinaryTree(0)
    dummy.left = root
    curr = dummy
    while curr:
        if curr.left:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                reverseDealNodes(curr.left, prev)
                prev.right = None
                curr = curr.right
        else:
            curr = curr.right


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, None, 2, 3]
    nums3 = ["b", "a", "f", None, None, "d", "g", None, None, None, None, "c", "e"]
    nums4 = range(10)
    bt = create_btree(nums4)
    post_order_traversal_iterative(bt)
