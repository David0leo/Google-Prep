import BinarySearchTree as BST

node1 = BST.BSTNode()
print(node1)
node1.set_value(1)
print(node1.get_value())

node2 = BST.BSTNode(2)
node2.set_parent(node1)
node1.set_right_child(node2)
print(node2)