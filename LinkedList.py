# =============================================
# Linked List in Python - Complete Tutorial
# Author: Intermediate Python Guide
# =============================================

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data       # stores the data
        self.next = None       # pointer to the next node
        # Time Complexity: O(1)

# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None       # initialize the head
        # Time Complexity: O(1)

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)           # O(1)
        new_node.next = self.head       # O(1)
        self.head = new_node            # O(1)
        # Overall Time Complexity: O(1)

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)           # O(1)
        if self.head is None:
            self.head = new_node        # O(1)
            return
        last = self.head
        while last.next:                # O(n)
            last = last.next
        last.next = new_node            # O(1)
        # Overall Time Complexity: O(n)

    # Insert after a given node
    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:  # O(n)
            current = current.next
        if not current:
            print("Previous node not found.")
            return
        new_node = Node(data)           # O(1)
        new_node.next = current.next    # O(1)
        current.next = new_node         # O(1)
        # Overall Time Complexity: O(n)

    # Delete node by value
    def delete_node(self, key):
        current = self.head
        # Case: head node to be deleted
        if current and current.data == key:  # O(1)
            self.head = current.next         # O(1)
            current = None
            return
        # Find the key to be deleted
        prev = None
        while current and current.data != key:  # O(n)
            prev = current
            current = current.next
        if not current:
            print("Node not found.")
            return
        prev.next = current.next             # O(1)
        current = None
        # Overall Time Complexity: O(n)

    # Search for a node by value
    def search(self, key):
        current = self.head
        while current:                       # O(n)
            if current.data == key:
                return True
            current = current.next
        return False
        # Time Complexity: O(n)

    # Traverse and print list
    def print_list(self):
        current = self.head
        while current:                       # O(n)
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        # Time Complexity: O(n)

    # Get the length of the linked list
    def length(self):
        count = 0
        current = self.head
        while current:                       # O(n)
            count += 1
            current = current.next
        return count
        # Time Complexity: O(n)

    # Reverse the linked list in-place
    def reverse(self):
        prev = None
        current = self.head
        while current:                       # O(n)
            next_node = current.next         # O(1)
            current.next = prev              # O(1)
            prev = current                   # O(1)
            current = next_node              # O(1)
        self.head = prev
        # Overall Time Complexity: O(n)

# ------------------------------
# Let's test the Linked List
# ------------------------------

# Create a Linked List
ll = LinkedList()

# Insert elements
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)
ll.insert_after(20, 25)

print("Original List:")
ll.print_list()  # 5 -> 10 -> 20 -> 25 -> 30 -> None

# Delete an element
ll.delete_node(10)
print("After deleting 10:")
ll.print_list()

# Search for an element
print("Is 25 in list?", ll.search(25))  # True
print("Is 100 in list?", ll.search(100))  # False

# Length of list
print("Length of list:", ll.length())  # 4

# Reverse the list
ll.reverse()
print("Reversed List:")
ll.print_list()