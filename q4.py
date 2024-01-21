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

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

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

def insert_avl(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    update_height(root)

    balance = balance_factor(root)

    # Left-Left case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right-Right case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left-Right case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right-Left case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def delete_avl(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        min_value = find_min(root.right)
        root.key = min_value
        root.right = delete_avl(root.right, min_value)

    update_height(root)

    balance = balance_factor(root)

    # Left-Left case
    if balance > 1 and balance_factor(root.left) >= 0:
        return right_rotate(root)

    # Left-Right case
    if balance > 1 and balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right-Right case
    if balance < -1 and balance_factor(root.right) <= 0:
        return left_rotate(root)

    # Right-Left case
    if balance < -1 and balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.key, end=" ")
        in_order_traversal(root.right)

# Example usage
avl_root = None

keys_to_insert = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for key in keys_to_insert:
    avl_root = insert_avl(avl_root, key)

print("AVL Tree after insertion:")
in_order_traversal(avl_root)

key_to_delete = 10
avl_root = delete_avl(avl_root, key_to_delete)

print("\nAVL Tree after deleting", key_to_delete, ":")
in_order_traversal(avl_root)
