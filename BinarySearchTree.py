class BSTNode:
    
    def __init__(self, key=None, value=None, parent=None, left_child=None, right_child=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    def set_left_child(self, new_left):
        self.left_child = new_left

    def set_right_child(self, new_right):
        self.right_child = new_right

    def set_key(self, new_key):
        self.key = new_key

    def set_value(self, new_value):
        self.value = new_value

    def get_parent(self):
        return self.parent

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_key(self):
        return self.key
    
    def get_value(self):
        return self.value



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
            if current_node.get_left_child():
                self._put(key, value, current_node.get_left_child())
            else:
                currentNode.set_left_child = BSTNode(key, value, current_node)
    
    def __setitem__(self, key, value):
        """Overloading [] operator for assignment.
           Allows for myTree['Red'] = 234
        """
        self.insert(key, value)