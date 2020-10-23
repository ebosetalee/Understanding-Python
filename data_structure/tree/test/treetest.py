import unittest
from tree.tree import Tree


class TestTree(unittest.TestCase):
    def test_root(self):
        tree = Tree("Electronics")
        self.assertIsNone(tree.parent)
        self.assertEqual(tree.children, [])

    def test_add_child(self):
        tree = Tree("Electronics")
        tree.add_child("laptop")
        tree.add_child("cellphone")
        tree.add_child("tv")
        self.assertIsNotNone(tree.children)

    def test_grand_child(self):
        tree = Tree("Electronics")

    def test_leaf_node(self):
        tree = Tree("Electronics")

    def test_display(self):
        tree = Tree("Electronics")
        pass


if __name__ == '__main__':
    unittest.main()
