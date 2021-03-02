# Python program to demonstrate
# insert operation in binary search tree


class Node:
    """
    A utility class that represents
    an individual node in a BST
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """
    A utility function to insert
    a new node with the given key
    :param root:
    :param key:
    :return:
    """
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    """
    # A utility function to do inorder tree traversal
    :param root:
    :return:
    """
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


if __name__ == '__main__':
    # Driver program to test the above functions
    # Let us create the following BST
    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80

    r = Node(1)
    r = insert(r, 2)
    r = insert(r, 3)
    r = insert(r, 4)
    r = insert(r, 5)
    r = insert(r, 6)
    r = insert(r, 7)

    # Print inoder traversal of the BST
    inorder(r)
