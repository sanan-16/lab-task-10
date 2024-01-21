class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return node.height

def update_height(node):
    if node is None:
        return 0
    node.height = 1 + max(height(node.left), height(node.right))
    return node.height

def left_rotate(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    update_height(y)
    update_height(x)

    return x

def right_rotate(x):
    y = x.left
    T2 = y.right

    y.right = x
    x.left = T2

    update_height(x)
    update_height(y)

    return y

def left_right_rotate(z):
    z.left = left_rotate(z.left)
    return right_rotate(z)

def right_left_rotate(z):
    z.right = right_rotate(z.right)
    return left_rotate(z)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Original AVL Tree:")
print(root.key)
print(root.left.key, root.right.key)
print(root.left.left.key, root.left.right.key)

# Perform left rotation
root = right_rotate(root)

print("\nAVL Tree after Right Rotation:")
print(root.key)
print(root.left.key, root.right.key)
print(root.left.left.key, root.left.right.key)

# Perform right rotation
root = left_rotate(root)

print("\nAVL Tree after Left Rotation:")
print(root.key)
print(root.left.key, root.right.key)
print(root.left.left.key, root.left.right.key)

# Perform left-right rotation
root = left_right_rotate(root)

print("\nAVL Tree after Left-Right Rotation:")
print(root.key)
print(root.left.key, root.right.key)
print(root.left.left.key, root.left.right.key)

# Perform right-left rotation
root = right_left_rotate(root)

print("\nAVL Tree after Right-Left Rotation:")
print(root.key)
print(root.left.key, root.right.key)
print(root.left.left.key, root.left.right.key)
