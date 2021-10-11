#  Node class
class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


#  Doubly Linked List class

class DoublyLinkedList:

    # Constructor
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    # Adds Node to head of DLList
    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node

        # If there is a current head, point it to new head
        if current_head is not None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        # Set new head as head_node of DLList
        self.head_node = new_head

        # Set new_head node as tail node if there is not one currently
        if self.tail_node is None:
            self.tail_node = new_head

        # Method to add Node to tail of DLList
        def add_to_tail(self, new_value):
            new_tail = Node(new_value)
            current_tail = self.tail_node

        # If there is a current tail, point it to new tail
            if current_tail is not None:
                current_tail.set_next_node(new_tail)
                new_tail.set_prev_node(current_tail)

            # Set DLList tail node value as new tail node
            self.tail_node = new_tail

            # Set new_tail node as head node if there is not one currently
            if self.head_node is None:
                self.head_node = new_tail

        # Removes head node from DLList
        def remove_head(self):
            removed_head = self.head_node

            # Checks if there is a head to remove
            if removed_head is None:
                return None

            # Change DLList head node to the next node in the list
            self.head_node = removed_head.get_next_node()

            # Sets new head_node's prev_node to None
            if self.head_node is not None:
                self.head_node.set_prev_node(None)

            # Removes the tail_node if the removed head node was also the tail_node
            if removed_head is self.tail_node:
                self.remove_tail()

            # Return the value of the removed head node
            return removed_head.get_value()
