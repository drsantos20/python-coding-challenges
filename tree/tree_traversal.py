# Python program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
in_order = []
pre_order = []
post_order = []


def print_in_order(root):

    if root:
        # First recur on left child
        print_in_order(root.left)

        # then print the data of node
        in_order.append(root.val),

        # now recur on right child
        print_in_order(root.right)

        return in_order


# A function to do postorder tree traversal
def print_post_order(root):

    if root:

        # First recur on left child
        print_post_order(root.left)

        # the recur on right child
        print_post_order(root.right)

        # now print the data of node
        post_order.append(root.val),

        return post_order


# A function to do preorder tree traversal
def print_pre_order(root):

    if root:
        # First print the data of node
        pre_order.append(root.val),

        # Then recur on left child
        print_pre_order(root.left)

        # Finally recur on right child
        print_pre_order(root.right)

        return pre_order
