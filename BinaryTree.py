class TreeNode:
    
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key=key
        self.data=data
        self.left=left
        self.right=right
    
    def __str__(self):
        return str(self.data)

class BinaryTree:
    
    def __init__(self, root=None):
        self.root = root
    
    def insert_left(self, new_node):
        if self.root.left == None:
            self.root.left = new_node
        else:
            