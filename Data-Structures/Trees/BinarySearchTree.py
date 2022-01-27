class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            # If there is no left node, we set left to equal value, and increase depth one level
            if self.left == None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                # If left value exists for this node, then we move the next left node and call insert on it
                self.left.insert(value)
        else:
            if self.right == None:
                # if there is no right node we set right to equal value, and increase depth one level
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                # If right value exists for this node then we move to the next right node then call insert again
                self.right.insert(value)


# Insert values below:

root = BinarySearchTree(100)
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)