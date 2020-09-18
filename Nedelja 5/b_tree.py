class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, current_node):
        if data < current_node.value:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.value:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The value is already in a tree")
            
bin_tree = BinaryTree(6)

'''
bin_tree.root.left = Node(3)
bin_tree.root.right = Node(7)
bin_tree.root.left.left = Node(2)
bin_tree.root.left.right = Node(5)
bin_tree.root.right.right = Node(9)
'''

bin_tree.insert(3)
bin_tree.insert(7)
bin_tree.insert(2)
bin_tree.insert(5)
bin_tree.insert(9)
