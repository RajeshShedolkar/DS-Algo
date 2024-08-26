class Node:
    """A Node class to represent each element in the linked list."""
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Points to the next node in the list


class LinkedList:
    """A LinkedList class to manage the operations on the linked list."""
    def __init__(self):
        self.head = None  # Initialize the linked list with the head node as None

    def append(self, data):
        """Add a node with the given data to the end of the linked list."""
        new_node = Node(data)  # Create a new node with the provided data

        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return

        # Traverse to the end of the list
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node  # Set the next of the last node to the new node

    def prepend(self, data):
        """Add a node with the given data at the beginning of the linked list."""
        new_node = Node(data)  # Create a new node with the provided data
        new_node.next = self.head  # Link the new node to the former head
        self.head = new_node  # Update the head to the new node

    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        if not self.head:
            return  # If the list is empty, do nothing

        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Traverse to find the node to be deleted
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:  # If the node to be deleted is found, skip it
            current.next = current.next.next

    def display(self):
        """Print all elements in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage of LinkedList
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.display()  # Output: 5 -> 10 -> 20 -> None
ll.delete(10)
ll.display()  # Output: 5 -> 20 -> None
