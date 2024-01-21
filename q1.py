class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def serialize(root):
    if root is None:
        return "None"

    left_str = serialize(root.left)
    right_str = serialize(root.right)

    return f"{root.key},{left_str},{right_str}"

def deserialize(data):
    def build_tree(values):
        value = values.pop(0)
        if value == "None":
            return None
        node = TreeNode(int(value))
        node.left = build_tree(values)
        node.right = build_tree(values)
        return node

    values = data.split(',')
    return build_tree(values)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

serialized_tree = serialize(root)
print("Serialized Tree:", serialized_tree)

deserialized_tree = deserialize(serialized_tree)
print("Deserialized Tree:")
print(deserialized_tree.key)  # Accessing the root key of the deserialized tree
