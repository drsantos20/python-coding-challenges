import unittest

from tree.tree_depth_or_height import Node, max_depth


class TestTreeMaxDepth(unittest.TestCase):

    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

    def test_tree_depth_order(self):
        self.assertEqual(3, max_depth(self.root))
