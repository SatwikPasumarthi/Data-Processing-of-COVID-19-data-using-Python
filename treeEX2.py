#PASUMARTHI SATWIK(19BCS083)
class node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)
def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)
root=node("A")
root.left=node("B")
root.right=node("C")
root.left.left=node("D")
root.left.right=node("E")
root.left.right.left=node("M")
root.right.left=node("F")
root.right.left.right=node("N")
root.right.right=node("G")
print("Inorder is")
printInorder(root)
print("Postorder is")
printPostorder(root)
print("Preorder is")
printPreorder(root)
