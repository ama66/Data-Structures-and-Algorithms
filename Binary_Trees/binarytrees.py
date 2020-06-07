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
        self.index=None        
      
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
    @property         
    def height(self):
        return self._height(self.root)
    
    def _height(self,root):
        if root==None:
            return 0 
        return 1+max(self._height(root.lchild),self._height(root.rchild))
        
    def create_tree(self):
        self.root=Node("P")
        self.root.lchild=Node("Q")
        self.root.rchild=Node("R")
        self.root.lchild.lchild=Node("A")
        self.root.lchild.rchild=Node("B")
        self.root.rchild.lchild=Node("X")
        
    @staticmethod  
    def search_index(A,data):
        for i,e in enumerate(A):
            if e==data:
                return i 
        return None
    
    def Construct_Tree_Pre_Inorder(self,inorder,preorder,startinorder,endinorder):
        
        self.index=0
        self.root=self._Construct_Tree_Pre_Inorder(inorder,preorder,startinorder,endinorder)
        return self 
    
    def _Construct_Tree_Pre_Inorder(self,inorder,preorder,startinorder,endinorder):
        ## pass in two arrays for inorder and preorder traversals and limiting indices for inorder array
        ## in the beginning we consider the whole array and then as we do recursive call we pass in limits
        ## of the left and right subtrees
        
        if startinorder > endinorder:
            return None
        
        # (1) take a node from the preorder array
        data = preorder[self.index]
        root=Node(data)
        self.index+=1
        
        if startinorder==endinorder:
            return root
        
        inorder_index = BinaryTree.search_index(inorder,data)
        
   
        
        root.lchild=self._Construct_Tree_Pre_Inorder(inorder,preorder,startinorder,inorder_index-1)
        root.rchild=self._Construct_Tree_Pre_Inorder(inorder,preorder,inorder_index+1,endinorder)
            
        return root
    
    def Construct_Tree_Post_Inorder(self,inorder,postorder,startinorder,endinorder):
        self.index=len(postorder)-1
        self.root=self._Construct_Tree_Post_Inorder(inorder,postorder,startinorder,endinorder)
        return self 
    
     
    def _Construct_Tree_Post_Inorder(self,inorder,postorder,startinorder,endinorder):
        ## pass in two arrays for inorder and preorder traversals and limiting indices for inorder array
        ## in the beginning we consider the whole array and then as we do recursive call we pass in limits
        ## of the left and right subtrees
        
        if startinorder > endinorder:
            return None
        
        # (1) take a node from the preorder array
        data = postorder[self.index]
        root=Node(data)
        self.index-=1

        if startinorder==endinorder:

            return root
        
        inorder_index = BinaryTree.search_index(inorder,data)
      
       
        root.rchild=self._Construct_Tree_Post_Inorder(inorder,postorder,inorder_index+1,endinorder)
        
        root.lchild=self._Construct_Tree_Post_Inorder(inorder,postorder,startinorder,inorder_index-1)

        

        return root  
        
        
                
        
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
print("\nTree height is ")
print(bt.height)
BinaryTree.search_index([3,4,5,6],6)


This is preorder traversal of the tree
P  Q  A  B  R  X  
This is inorder traversal of the tree
A  Q  B  P  X  R  
This is postorder traversal of the tree
A  B  Q  X  R  P  
This is level order traversal of the tree
P  Q  R  A  B  X  
Tree height is 
3

3


#              A
#          /       \
#        B           C
#     /     \       /
#    D      E     F
inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
preOrder = ['A', 'B', 'D', 'E', 'C', 'F'] 

newtree=BinaryTree()
newtree.Construct_Tree_Pre_Inorder(inOrder,preOrder,0,len(inOrder)-1).inorder()

D  B  E  A  F  C  

inOrder = ['D', 'B', 'E', 'A', 'F', 'C'] 
postOrder = ['D', 'E', 'B', 'F', 'C', 'A'] 
newtr=BinaryTree()
newtr.Construct_Tree_Post_Inorder(inOrder,postOrder,0,len(inOrder)-1).inorder()

D  B  E  A  F  C  

