#PASUMARTHI SATWIK(19BCS083)
# The Tree I am using is:
#                  A
#                /   \
#               B      C
#             /  \    /
#            D    E  F
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
root.right=node("U")
root.left.left=node("S")
root.left.left.left=node("W")
root.left.left.left.left=node("Z")
root.left.right=node("R")
root.left.right.left=node("Y")
root.left.right.right=node("A")
root.right.left=node("E")
root.right.right=node("P")
root.right.right.left=node("G")
root.right.right.right=node("J")
print("Inorder is")
printInorder(root)
print("Postorder is")
printPostorder(root)
print("Preorder is")
printPreorder(root)
