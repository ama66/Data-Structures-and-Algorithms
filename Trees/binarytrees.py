## implement Binary Tree methods

class Node:
class Node:
    def __init__(self,info):
        self.info=info
        self.lchild=None
        self.rchild=None
        
class BinaryTree:
    def __init__(self):
        self.root=None
    def preorder(self):
        self._preorder(self.root)
        print()
    
    def _preorder(self,rootnode):
        if rootnode==None:
            return
        print(rootnode.info, " ", end="")
        self._preorder(rootnode.lchild)
        self._preorder(rootnode.rchild)
        
    def create_tree(self):
        self.root=Node("P")
        self.root.lchild=Node("Q")
        self.root.rchild=Node("R")
        self.root.lchild.lchild=Node("A")
        self.root.lchild.rchild=Node("B")
        self.root.rchild.lchild=Node("X")
        
bt=BinaryTree()
bt.create_tree()
print("This is preorder traversal of the tree")
bt.preorder()

