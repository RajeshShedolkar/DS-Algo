class Node:
    """A Node class to represent each element in the doubly linked list."""
    def __init__(self, data):
        self.data = data   # Stores data
        self.next = None   # Points to the next node in the list
        self.prev = None   # Points to the previous node in the list


class DoublyLinkedList:
    """A DoublyLinkedList class to manage the operations on the doubly linked list."""
    def __init__(self):
        self.head = None   # Initialize the doubly linked list with the head node as None

    def append(self, data):
        """Add a node with the given data to the end of the doubly linked list."""
        new_node = Node(data)  # Create a new node with the provided data

        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return

        # Traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node  # Set the next of the last node to the new node
        new_node.prev = last_node  # Set the previous of the new node to the last node

    def prepend(self, data):
        """Add a node with the given data at the beginning of the doubly linked list."""
        new_node = Node(data)  # Create a new node with the provided data

        new_node.next = self.head  # Link the new node to the former head
        if self.head:
            self.head.prev = new_node  # Set the previous of the old head to the new node
        self.head = new_node  # Update the head to the new node

    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        if not self.head:
            return  # If the list is empty, do nothing

        current = self.head

        # If the node to be deleted is the head
        if current.data == data:
            self.head = current.next  # Move head to the next node
            if self.head:
                self.head.prev = None  # Update the new head's prev to None
            return

        # Traverse to find the node to be deleted
        while current and current.data != data:
            current = current.next

        if current:  # If the node to be deleted is found
            if current.next:  # If it is not the last node
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next

    def display(self):
        """Print all elements in the doubly linked list from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Example usage of DoublyLinkedList
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.display()  # Output: 5 <-> 10 <-> 20 <-> None
dll.delete(10)
dll.display()  # Output: 5 <-> 20 <-> None
