class BSTNode:
    
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right

    def set_key(self, new_key):
        self.key = new_key

    def set_value(self, new_value):
        self.value = new_value

    def get_parent(self):
        return self.parent

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value
    
    def is_left_child(self):
        return self.parent and self.parent.left == self
    
    def is_right_child(self):
        return self.parent and self.parent.right == self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.right or self.left)
    
    def replace_data(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __str__(self):
        return str(self.key)

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


    def insert(self, key, value):
        if self.root:
            self.root._insert(key, value, self.root)
        else:
            self.root = BSTNode(key, value)
        self.size = self.size + 1

    def _insert(self, key, value, current_node):
        if key < current_node.get_key():
            if current_node.get_left():
                self._put(key, value, current_node.get_left())
            else:
                currentNode.set_left(BSTNode(key, value, current_node))
        else:
            if current_node.get_right():
                self._insert(key, value, current_node.get_right())
            else:
                current_node.set_right(BSTNode(key, value, current_node))
    
    def __setitem__(self, key, value):
        """Overloading [] operator for assignment.
           Allows for myTree['Red'] = 234
        """
        self.insert(key, value)