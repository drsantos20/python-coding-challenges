# Python program to print level order traversal using Queue


# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative Method to print the height of binary tree
def level_order(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    node_level_order = []

    # Enqueue Root and initialize height
    queue.append(root)

    while len(queue) > 0:
        # Print front of  queue and remove it from queue
        node_level_order.append(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

    return node_level_order

