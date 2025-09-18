# -------------------------------------
# BINARY TREE - KEY CONCEPTS & ALGORITHMS
# -------------------------------------

# --- Definition ---
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # Left child
        self.right = None  # Right child


# --- TYPES OF BINARY TREES ---
# 1. Full Binary Tree: Every node has 0 or 2 children
# 2. Complete Binary Tree: All levels are completely filled except the last,
#    and all nodes are as left as possible.
# 3. Perfect Binary Tree: All internal nodes have two children and all leaves are at same level.
# 4. Balanced Binary Tree: Height difference between left and right subtree of any node is ≤ 1
# 5. Degenerate Tree: Each parent node has only one child (like a linked list)


# --- TRAVERSAL METHODS ---

# Inorder Traversal (Left → Root → Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)

# Preorder Traversal (Root → Left → Right)
def preorder(node):
    if node:
        print(node.val, end=' ')
        preorder(node.left)
        preorder(node.right)

# Postorder Traversal (Left → Right → Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=' ')

# Level Order Traversal (BFS using Queue)
from collections import deque
def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# --- INSERTION IN BINARY TREE (Level Order to keep it complete) ---
def insert(root, key):
    new_node = TreeNode(key)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = new_node
            return
        else:
            queue.append(node.left)
        if not node.right:
            node.right = new_node
            return
        else:
            queue.append(node.right)


# --- DELETION IN BINARY TREE (Replace with deepest node) ---
def delete(root, key):
    if not root:
        return None
    if root.left is None and root.right is None:
        return None if root.val == key else root
    
    # Step 1: Find node to delete and deepest node
    key_node = None
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.val == key:
            key_node = temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    if key_node:
        key_node.val = temp.val  # Replace with deepest node's value
        delete_deepest(root, temp)
    return root

def delete_deepest(root, del_node):
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.left:
            if temp.left == del_node:
                temp.left = None
                return
            queue.append(temp.left)
        if temp.right:
            if temp.right == del_node:
                temp.right = None
                return
            queue.append(temp.right)


# --- HEIGHT / DEPTH OF TREE ---
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
# Time Complexity: O(n)


# --- CHECK FULL BINARY TREE ---
def is_full_tree(node):
    if not node:
        return True
    if not node.left and not node.right:
        return True
    if node.left and node.right:
        return is_full_tree(node.left) and is_full_tree(node.right)
    return False


# --- CHECK PERFECT BINARY TREE ---
def is_perfect(root):
    def depth(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d
    
    def is_perfect_util(node, d, level=0):
        if not node:
            return True
        if not node.left and not node.right:
            return d == level + 1
        if not node.left or not node.right:
            return False
        return is_perfect_util(node.left, d, level + 1) and is_perfect_util(node.right, d, level + 1)

    return is_perfect_util(root, depth(root))


# --- CHECK COMPLETE BINARY TREE ---
def is_complete_tree(root):
    if not root:
        return True
    queue = deque([root])
    end = False
    while queue:
        node = queue.popleft()
        if node:
            if end:
                return False
            queue.append(node.left)
            queue.append(node.right)
        else:
            end = True
    return True


# --- CHECK IF TREE IS BALANCED (Height-balanced) ---
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:
            return -1
        right = check(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    return check(root) != -1


# --- LOWEST COMMON ANCESTOR (LCA) ---
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right
# Time Complexity: O(n)


# --- DIAMETER OF BINARY TREE ---
def diameter(root):
    max_diameter = [0]
    
    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        max_diameter[0] = max(max_diameter[0], left + right)
        return 1 + max(left, right)

    dfs(root)
    return max_diameter[0]
# Time Complexity: O(n)


# --- COMMON TIME COMPLEXITIES ---
# Traversals (Inorder, Preorder, Postorder, Level): O(n)
# Insertion/Deletion (Unordered Binary Tree): O(n)
# Height Calculation: O(n)
# LCA, Diameter: O(n)
# Checking Full/Complete/Perfect: O(n)


# Level 1
root = TreeNode(1)

# Level 2
root.left = TreeNode(2)
root.right = TreeNode(3)

# Level 3
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# ------------------------------
# Test All Functions
# ------------------------------

print("Inorder Traversal:")     # Expected: 4 2 5 1 6 3 7
inorder(root)
print("\nPreorder Traversal:")  # Expected: 1 2 4 5 3 6 7
preorder(root)
print("\nPostorder Traversal:") # Expected: 4 5 2 6 7 3 1
postorder(root)
print("\nLevel Order Traversal:")  # Expected: 1 2 3 4 5 6 7
level_order(root)

print("\n\nHeight of Tree:", height(root))  # Expected: 3

print("Is Full Tree:", is_full_tree(root))  # Expected: True
print("Is Perfect Tree:", is_perfect(root)) # Expected: True
print("Is Complete Tree:", is_complete_tree(root)) # Expected: True
print("Is Balanced Tree:", is_balanced(root))      # Expected: True

# LCA test
node4 = root.left.left       # Node 4
node5 = root.left.right      # Node 5
lca_node = lca(root, node4, node5)
print("LCA of 4 and 5:", lca_node.val if lca_node else None)  # Expected: 2

# Diameter
print("Diameter of Tree:", diameter(root))  # Expected: 4 (path = 4-2-1-3-7)

# Insertion (adds level-wise)
print("\nInserting node with value 8...")
insert(root, 8)
print("Level Order after insertion:")
level_order(root)  # Should include 8 at the left of node 4/5/6/7 depending on position

# Deletion
print("\n\nDeleting node with value 3...")
delete(root, 3)
print("Level Order after deletion:")
level_order(root)  # Node 3 should be replaced with the deepest node
