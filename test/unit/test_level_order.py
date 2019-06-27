import unittest

from tree.tree_level_order import Node, level_order


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

    def test_tree_level_order(self):
        self.assertListEqual([1, 2, 3, 4, 5], level_order(self.root))
