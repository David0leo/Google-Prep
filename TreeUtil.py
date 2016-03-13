def rprint_preorder(root):
    if root:
        print(root)
        rprint_preorder(root.left)
        rprint_preorder(root.right)
    return

def rprint_inorder(root):
    if root:
        rprint_inorder(root.left)
        print(root)
        rprint_inorder(root.right)
    return

def rprint_postorder(root):
    if root:
        rprint_postorder(root.left)
        rprint_postorder(root.right)
        print(root)
    return