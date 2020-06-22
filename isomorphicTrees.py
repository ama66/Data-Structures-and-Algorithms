## Check if two binary trees are isomorphic (structurally similar even though may take different forms)
#################

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
      
def Is_Isomorphic(node1, node2): 
    
    if node1 is None and node2 is None: 
        return True
  
    if node1 is None or node2 is None: 
        return False
  
    if node1.data != node2.data : 
        return False

    return ((Is_Isomorphic(node1.left, node2.left)and 
            Is_Isomorphic(node1.right, node2.right)) or
            (Is_Isomorphic(node1.left, node2.right) and 
            Is_Isomorphic(node1.right, node2.left)) 
            ) 
####      1
##      /   \ 
###    2     3 
##    / \   /
##   4   5  6 
#       / \ 
#      7  8
# Driver program to test above function 
Node1 = Node(1) 
Node1.left = Node(2) 
Node1.right = Node(3) 
Node1.left.left = Node(4) 
Node1.left.right = Node(5) 
Node1.right.left = Node(6) 
Node1.left.right.left = Node(7) 
Node1.left.right.right = Node(8) 

####       1
##      /     \ 
###    3       2 
##      \     / \
##       6   4   5 
##              /  \ 
##             8    7

Node2 = Node(1) 
Node2.left = Node(3) 
Node2.right = Node(2) 
Node2.right.left = Node(4) 
Node2.right.right = Node(5) 
Node2.left.right = Node(6) 
Node2.right.right.left = Node(8) 
Node2.right.right.right  = Node(7) 
  
Is_Isomorphic(Node1, Node2) 
  
True

