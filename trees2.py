#PASUMARTHI SATWIK(19BCS083)
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(node):
    if node is None:
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)
        if(lheight > rheight):
            return lheight+1
        else:
            return rheight+1
def prtLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printlevel(root, i)
def printlevel(root,level):
    if root is None:
        return None
    if (level==1):
        print(root.data)
    elif level > 1:
        printlevel(root.left,level-1)
        printlevel(root.right,level-1)
root=Node("A")
root.left=Node("B")
root.right=Node("U")
root.left.left=Node("S")
root.left.left.left=Node("W")
root.left.left.left.left=Node("Z")
root.left.right=Node("R")
root.left.right.left=Node("Y")
root.left.right.right=Node("A")
root.right.left=Node("E")
root.right.right=Node("P")
root.right.right.left=Node("G")
root.right.right.right=Node("J")
print("Levelorder traversal is \n")
prtLevelOrder(root)