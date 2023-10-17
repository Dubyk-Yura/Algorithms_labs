import unittest
from src.binary_diameter import find_longer_diameter, BinaryTree


class TestDiameter(unittest.TestCase):
    def test_condition_example(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)
        result = find_longer_diameter(root)
        self.assertEqual(result, 6)

    def test_two_branches(self):
        root = BinaryTree(1)
        root.right = BinaryTree(10)
        root.right.right = BinaryTree(2)
        root.right.right.right = BinaryTree(3)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(9)
        root.left.left.left.left = BinaryTree(11)
        result = find_longer_diameter(root)
        self.assertEqual(result, 7)

    def test_filled_tree(self):
        root = BinaryTree(1)
        root.right = BinaryTree(10)
        root.right.right = BinaryTree(2)
        root.right.right.right = BinaryTree(3)
        root.right.right.left = BinaryTree(12)
        root.right.left = BinaryTree(15)
        root.right.left.left = BinaryTree(13)
        root.right.left.right = BinaryTree(14)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(9)
        root.left.left.right = BinaryTree(4)
        root.left.right = BinaryTree(6)
        root.left.right.left = BinaryTree(8)
        root.left.right.right = BinaryTree(11)
        result = find_longer_diameter(root)
        self.assertEqual(result, 6)
