class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


max_diameter = 0


def find_longer_diameter(node: BinaryTree) -> int:
    global max_diameter
    node.left_depth = 0
    node.right_depth = 0
    if node.left is not None:
        find_longer_diameter(node.left)
        node.left_depth = node.left.longer_depth + 1
    if node.right is not None:
        find_longer_diameter(node.right)
        node.right_depth = node.right.longer_depth + 1
    node.longer_depth = max(node.right_depth, node.left_depth)
    if node.right_depth + node.left_depth > max_diameter:
        max_diameter = node.right_depth + node.left_depth
    return max_diameter
