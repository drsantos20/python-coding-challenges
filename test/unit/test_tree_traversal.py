import unittest

from tree.tree_traversal import (Node,
                                 print_in_order,
                                 print_pre_order,
                                 print_post_order,
                                 )


class TestTreeTraversal(unittest.TestCase):

    def setUp(self):
        self.node = Node
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

    def test_tree_traversal_in_order(self):
        self.assertListEqual([4, 2, 5, 1, 3], print_in_order(self.root))

    def test_tree_traversal_pre_order(self):
        self.assertListEqual([1, 2, 4, 5, 3], print_pre_order(self.root))

    def test_tree_traversal_post_order(self):
        self.assertListEqual([4, 5, 2, 3, 1], print_post_order(self.root))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTreeTraversal)
    unittest.TextTestRunner(verbosity=2).run(suite)
