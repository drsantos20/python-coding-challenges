# Python3 program to find the maximum depth of tree 


# A binary tree node 
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Compute the "maxDepth" of a tree -- the number of nodes  
# along the longest path from the root node down to the  
# farthest leaf node 
def max_depth(node):
    if node is None:
        return 0

    else:
        # Compute the depth of each subtree
        left_node_with_longest_depth = max_depth(node.left)
        right_node_with_longest_depth = max_depth(node.right)

    # Use the larger one
    if left_node_with_longest_depth > right_node_with_longest_depth:
        return left_node_with_longest_depth + 1
    else:
        return right_node_with_longest_depth + 1


# Driver program to test above function 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of tree is %d" % (max_depth(root)))
