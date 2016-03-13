class TreeNode:
    
    def __init__(self, key=None, data=None, parent=None, left=None, right=None):
        self.key = key
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
    
class AVLTree:
    """Assumes right child higher"""
    
    def __init__(self, root=None):
        
        self.root = root
    
    def fix_avl(self, node):
        """
        Fix AVL property from changed
        node up. Find lowest node x violating AVL.
        """
        #if x.right is right heavy or balanced
        #left rotate x
        
        #else
        #right rotate x.right, left rotate x