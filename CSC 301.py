# Node class
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def insert_at_beginning(self, data):  
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print("Key not found.")
            return

        prev.next = current.next

    def display_list(self):
        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        print("None")


# Testing
list = LinkedList()

list.insert_at_end(10)
list.insert_at_end(20)
list.insert_at_end(30)
list.insert_at_end(40)
list.insert_at_end(50)

print("Initial list:")
list.display_list()

list.delete_node(30)
print("After deleting 30:")
list.display_list()