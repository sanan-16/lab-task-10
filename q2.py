class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def diameter_of_binary_tree(root):
    def height_and_diameter(node):
        if node is None:
            return 0, 0

        left_height, left_diameter = height_and_diameter(node.left)
        right_height, right_diameter = height_and_diameter(node.right)

        current_height = max(left_height, right_height) + 1
        current_diameter = max(left_height + right_height, left_diameter, right_diameter)

        return current_height, current_diameter

    _, diameter = height_and_diameter(root)
    return diameter

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = diameter_of_binary_tree(root)
print("Diameter of the binary tree:", result)
