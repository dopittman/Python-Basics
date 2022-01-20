
class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        # Python's list comprehension combines a for loop and conditional then returns a new list
        # ie. For child in self.children
        #       if child is not child_node
        #       new_list.append(child)

        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        # Add current node in list of nodes to visit
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            # pop the current node off the duplicate tree
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            # add the children of the popped node to the list of nodes to visit
            nodes_to_visit += current_node.children

root = TreeNode("CEO of Bananas")
child_a = TreeNode("VP of Bananas")
child_b = TreeNode("Assistant VP of bananas")
child_c = TreeNode("Executive Assistant of Bananas")
root.add_child(child_a)
child_a.add_child(child_b)
root.add_child(child_c)
root.traverse()
