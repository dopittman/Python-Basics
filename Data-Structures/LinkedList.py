from Node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Create a new head_node and attach it to the beginning of the LL
    def insert_beginning(self, new_value):
        new_node = Node(new_value, self.head_node)
        self.head_node = new_node
