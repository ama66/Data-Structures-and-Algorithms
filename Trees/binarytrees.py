## implement Binary Tree methods

from collections import deque
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
        
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self,rootnode):
        if rootnode==None:
            return
        self._inorder(rootnode.lchild)
        print(rootnode.info, " ", end="")
        self._inorder(rootnode.rchild)
        
    def postorder(self):
        self._postorder(self.root)
        print()
    
    def _postorder(self,rootnode):
        if rootnode==None:
            return
        self._postorder(rootnode.lchild)
        self._postorder(rootnode.rchild)
        print(rootnode.info, " ", end="")
        

    def levelorder(self):
        qu=deque()
        qu.append(self.root)
        while len(qu)!=0:
            p=qu.popleft()
            print(p.info, " ", end="")
            if p.lchild:
                qu.append(p.lchild)
            if p.rchild:
                qu.append(p.rchild)
                

        
        
        
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
print("This is inorder traversal of the tree")
bt.inorder()
print("This is postorder traversal of the tree")
bt.postorder()
print("This is level order traversal of the tree")
bt.levelorder()

This is preorder traversal of the tree
P  Q  A  B  R  X  
This is inorder traversal of the tree
A  Q  B  P  X  R  
This is postorder traversal of the tree
A  B  Q  X  R  P  
This is level order traversal of the tree
P  Q  R  A  B  X  
