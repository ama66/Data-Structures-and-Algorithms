def convertbstdll(root):
    ## Think about base case after you reach a lead.
    ## the recursion should return a doubly linked list from left and right subtrees
    ## we could then splice them together with the root in the middle 
    
    if root==None:
        return None
    elif root.left==None and root.right==None:
        return [root,root]
    
    leftdll=convertbstdll(root.left)
    rightdll=convertbstdll(root.right)
    
    ## Now leftdll and rightdll are lists containing head and tail of doubly linked lists
    # Now we need to connect them to creat the [head] and tail of the combined dlls and root
    head=None
    tail=None
    
    if leftdll==None:
        head=root
    else:
        leftdll[1].right=root
        root.left=leftdll[1]
        head=leftdll[0]
        
    if rightdll==None:
        tail=root
    else:
        rightdll[0].left=root
        root.right=rightdll[0]
        tail=rightdll[1]
        
    return [head,tail]

leaf1 = Node(4)
leaf2 = Node(7)

leaf3 = Node(11)
leaf4 = Node(14)

leaf5 = Node(37)

leaf6 = Node(17)

node1 = Node(5, leaf1, leaf2)
node2 = Node(12, leaf3, leaf4)
node3 = Node(39, leaf5, None)

node4 = Node(32, leaf6, node3)

node5 = Node(1, None, node1)

node6 = Node(10, node5, node2)


root = Node(15, node6, node4)

    
head,tail = convertbstdll(root)



while head:
    print(head.val)
    head = head.right

print("************")

while tail:
    print(tail.val)
    tail = tail.left


1
4
5
7
10
11
12
14
15
17
32
37
39
**************
39
37
32
17
15
14
12
11
10
7
5
4
1
 
