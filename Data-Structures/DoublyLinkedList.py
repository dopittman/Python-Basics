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
