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
            try: 
                print(p.info, " ", end="")
                if p.lchild:
                    qu.append(p.lchild)
                if p.rchild:
                    qu.append(p.rchild)
            except:
                pass
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
    
    def delete(self,x):
        self.root=self._delete(self.root,x)
        
        
    def _delete(self,p,x):
        ## Recursion could end If I cannot find x and I end up in a None node after honing in on x
        if p==None:
            print(x , " cannot be found")
            return p
        ## Other recursive path is to end up finding x 
        if x < p.info:
            p.lchild=self._delete(p.lchild,x)
        elif x > p.info:
            p.rchild=self._delete(p.rchild,x)
        else:
            ## Found node to be deleted
            #Case where the node to be deleted has two children 
             if p.lchild is not None and p.rchild is not None:
                # find inorder successor of the node p and replace it by that node
                s=p.rchild 
                while s.lchild is not None:
                    s=s.lchild 
                p.info=s.info
                ## Now starting at subtree rooted at p.rchild delete s.info 
                p.rchild=self._delete(p.rchild, s.info)
                 
             else: # case where I have either one child or None 
                ## Find if I have left or right child and assign a value for child pointer ch
                if p.lchild is not None:
                    ch=p.lchild
                else:
                    ch=p.rchild 
                ## let p = child 
                p=ch
            
        return p 
        
        
    def delete1(self,x):
        """ Iterative implementation"""
        ## First find node to be deleted x start the search at the root 
        p=self.root 
        par=None # parent of the root initially none 
        ## Traverse the tree looking for the node x and update parent
        while p is not None:
            if p.info==x:
                break 
            par=p
            if p.info < x: 
                p=p.rchild 
            else: 
                p=p.lchild 
                
        if p==None:
            print(x, "Cannot be found in the BS Tree")
            return 
        ## if this is not the case then x was found and p refers to this node 
        # and par is its parent. Now we have two possibilities
        # C) p has two children 
        if p.lchild is not None and p.rchild is not None:
            # find inorder successor of the node p and replace it by that node
            s=p.rchild 
            s_par=p
            while s.lchild is not None:
                s_par=s
                s=s.lchild 
            ## Now reduce the delete problem to another one in which the node
            ## can have either one or no children. This is one of these cases
            ## where s does not have left child but the later part of the code
            ## will handle the two cases where the node could have either left or right child
            ## and the other one is missing
            p=s
            par=s_par
        
        ## Case where p has left child and no right child
        if p.lchild is not None:
            ch=p.lchild 
        else:
            ch=p.rchild 
        ## Now I determined the child of the node to be deleted.
        # and I know its parent par!
        if par==None:
            self.root=ch
        elif p==par.lchild:
            par.lchild=ch
        else:
            par.rchild=ch
        
     
        
        
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
25  20  35  18  23  35  25  20  35  18  23  35  5  


bt.delete1(5)
bt.levelorder()


bt.delete1(5)

bt.levelorder()

25  20  35  18  23  35  

bt.delete1(35)
bt.levelorder()

25  20  35  18  23  
