from collections import deque

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def search(self,val):
        return self._search(self.root,val)
    
    def _search(self,root,val):
        """ Recursive implementation"""
        if root==None:
            return None 
        elif root.info > val:
            return self._search(root.lchild,val)
        elif root.info < val:
            return self._search(root.rchild,val)
        else:
            return root

    def search1(self,val):
        return self._search1(self.root,val)
    
    def _search1(self,root,val):
        """Iterative implementation"""
        p=root
        while p:
            if p.info > val : 
                p=p.lchild
            elif p.info < val : 
                p=p.rchild
            else:
                return p 
        return None 
            
            
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
    
    def max(self):
        return self._max(self.root)
    
    def _max(self,root):
        if root.rchild is not None:
            return self._max(root.rchild)
        else:
            return root 
    def max1(self):
        p=self.root
        while p.rchild:
            p=p.rchild
        return p 
    
    def min(self):
        return self._min(self.root)
    
    def _min(self,root):
        if root.lchild is not None:
            return self._min(root.lchild)
        else:
            return root 
    def min1(self):
        p=self.root
        while p.lchild:
            p=p.lchild
        return p 
    
    def insert(self,x):
        self.root=self._insert(self.root, x)
    
    def _insert(self,p,x):
        """ insert x at node rooted at p """
        if p is None:
            p=Node(x)
        elif p.info > x : 
            p.lchild=self._insert(p.lchild,x)
        elif p.info < x : 
            p.rchild=self._insert(p.rchild,x)
        else:
            print("node ", x ," already exist in tree")
            return 
            
        return p 
    
    
    def insert1(self,x):
        # find where the node belongs 
        p=self.root
        if p==None:
            p=Node(x)
            return 
        
        while p is not None: 
            parent=p 
            if p.info > x :
                p=p.lchild 
            elif p.info < x : 
                p=p.rchild 
            else:
                print("\nnode ", x ," already exist in tree")
                break 
                
        if parent.info > x:    
            parent.lchild=Node(x)
        elif parent.info < x :
            parent.rchild=Node(x)
    
            
        return 
    
        
        
    def create_tree(self):
            self.root=Node(25)
            self.root.lchild=Node(20)
            self.root.rchild=Node(35)
            self.root.lchild.lchild=Node(18)
            self.root.lchild.rchild=Node(23)
            self.root.rchild.lchild=Node(35)
#              25
#          /       \
#       20          35
#     /     \       /
#    18     23    30

bt=BinarySearchTree()
bt.create_tree()
bt.levelorder()
node_to_search = bt.search(18)
if node_to_search:
    print("\nFound Node Recursively: ", node_to_search.info)
    
node_to_search = bt.search1(18)
if node_to_search:
    print("\nFound Node Iteratively: ", node_to_search.info)

node_to_search = bt.search(110)
if node_to_search is None :
    print("\n Did not Find Node 110 Recursively: ")
    
node_to_search = bt.search1(110)
if node_to_search is None:
    print("\n Did not Find Node 110 Iteratively: ")
    
max_node=bt.max()
if max_node:
    print("Max node found: ", max_node.info)
max_node1=bt.max1()
if max_node1:
    print("Max node found: ", max_node1.info)
min_node=bt.min()
if max_node:
    print("Min node found: ", min_node.info)
min_node1=bt.min1()
if min_node1:
    print("Min node found: ", min_node1.info)
    
#              25
#          /       \
#       20          35
#     /     \       /
#    18     23    30

    
    25  20  35  18  23  35  
Found Node Recursively:  18

Found Node Iteratively:  18

 Did not Find Node 110 Recursively: 

 Did not Find Node 110 Iteratively: 
Max node found:  35
Max node found:  35
Min node found:  18
Min node found:  18

bt.insert1(50)
bt.levelorder()
bt.insert1(50)
bt.levelorder()

25  20  35  18  23  35  50  
node  50  already exist in tree
25  20  35  18  23  35  50  


#              25
#          /       \
#       20          35
#     /     \       / \ 
#    18     23    30   50 
# 5 /

bt.insert(50)
bt.levelorder()
bt.insert(5)
bt.levelorder()

node  50  already exist in tree
25  20  35  18  23  35  50  5  node  5  already exist in tree
25  20  35  18  23  35  50  5  

