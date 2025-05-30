"""
==============================
LINKED LIST IN PYTHON - SUMMARY
==============================

A linked list is a linear data structure where each element (node) points to the next. 
Each node contains:
- Data
- Pointer to the next node

Types:
1. Singly Linked List (each node points to next)
2. Doubly Linked List (each node points to next and previous)
3. Circular Linked List (last node points to head)

Operations:
- Insertion (at head, tail, index)
- Deletion (by value or position)
- Traversal
- Reversal
- Search
"""

# -------------------------
# Node class for singly linked list
# -------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# -------------------------
# Printing a linked list
# -------------------------
def print_list(head):
    """Traverse and print the linked list"""
    curr = head
    while curr:
        print(curr.data, end=' -> ')
        curr = curr.next
    print("None")

# -------------------------
# Insert at head
# -------------------------
def insert_at_head(head, data):
    """Insert new node at the beginning"""
    new_node = Node(data)
    new_node.next = head
    return new_node

# -------------------------
# Insert at tail
# -------------------------
def insert_at_tail(head, data):
    """Insert new node at the end"""
    new_node = Node(data)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

# -------------------------
# Insert at a specific index
# -------------------------
def insert_at_index(head, data, index):
    """Insert new node at a specific index"""
    if index == 0:
        return insert_at_head(head, data)
    new_node = Node(data)
    curr = head
    for _ in range(index - 1):
        if not curr:
            return head  # Index out of bounds
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head

# -------------------------
# Delete by value
# -------------------------
def delete_by_value(head, value):
    """Delete the first occurrence of value"""
    if not head:
        return None
    if head.data == value:
        return head.next
    curr = head
    while curr.next and curr.next.data != value:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
    return head

# -------------------------
# Search for a value
# -------------------------
def search(head, target):
    """Search for a value in the linked list"""
    curr = head
    while curr:
        if curr.data == target:
            return True
        curr = curr.next
    return False

# -------------------------
# Reverse a linked list
# -------------------------
def reverse_list(head):
    """Reverse the linked list in-place"""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# -------------------------
# Convert linked list to Python list
# -------------------------
def to_pylist(head):
    """Convert linked list to Python list"""
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result

# -------------------------
# MAIN DEMO
# -------------------------
# Build a linked list from scratch
head = None
head = insert_at_head(head, 3)
head = insert_at_head(head, 2)
head = insert_at_head(head, 1)
print("Initial list:")
print_list(head)

# Insert at tail
head = insert_at_tail(head, 4)
head = insert_at_tail(head, 5)
print("After inserting at tail:")
print_list(head)

# Insert at index
head = insert_at_index(head, 9, 2)
print("After inserting 9 at index 2:")
print_list(head)

# Delete a node by value
head = delete_by_value(head, 3)
print("After deleting value 3:")
print_list(head)

# Search for a value
print("Search for 9:", search(head, 9))      # True
print("Search for 100:", search(head, 100))  # False

# Reverse the list
head = reverse_list(head)
print("After reversing the list:")
print_list(head)

# Convert to Python list
print("Python list version:", to_pylist(head))


"""
===============================
DOUBLY LINKED LIST - OPTIONAL
===============================

Each node stores:
- data
- pointer to next node
- pointer to previous node

Allows traversal in both directions.
"""

# Node for doubly linked list
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Print doubly linked list forward
def print_doubly_forward(head):
    curr = head
    while curr:
        print(curr.data, end=' <-> ')
        last = curr
        curr = curr.next
    print("None")
    return last  # return last node for backward print

# Print doubly linked list backward
def print_doubly_backward(tail):
    curr = tail
    while curr:
        print(curr.data, end=' <-> ')
        curr = curr.prev
    print("None")

# Insert at head in doubly linked list
def insert_doubly_head(head, data):
    new_node = DNode(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

# Demo doubly linked list
dhead = None
dhead = insert_doubly_head(dhead, 10)
dhead = insert_doubly_head(dhead, 20)
dhead = insert_doubly_head(dhead, 30)
print("Doubly Linked List forward:")
tail = print_doubly_forward(dhead)
print("Doubly Linked List backward:")
print_doubly_backward(tail)

# End of Linked List Summary
