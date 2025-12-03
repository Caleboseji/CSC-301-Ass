# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete a node by key (value)
    def delete_node(self, key):
        current = self.head

        # If head node is the one to delete
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If value not found
        if current is None:
            print(f"{key} not found in list.")
            return

        # Unlink the node
        prev.next = current.next

    # Display the list
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ----------------------------
# TEST THE LINKED LIST
# ----------------------------

ll = LinkedList()

# Insert at least 5 values
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)

print("Initial Linked List:")
ll.display_list()

# Delete one value
ll.delete_node(30)

print("After deleting 30:")
ll.display_list()

