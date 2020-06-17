class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        
# Example Input:
# 1 <---> 2
# ^       ^
# |       |
# v       v
# 4 <---> 3

# Example Output:

# 1 <---> 2
# ^       ^
# |       |
# v       v
# 4 <---> 3

# Visited nodes as we traverse
# DFS - Depth First Search
# apply recursion

def clone_helper(node, visited):
    ## this if may not be necessary!
    if node == None:
        return None
    ## note that node 2 is a neighbor of node 1 and node 1 is also a neighbor of 2 
    ## so one needs to return visited[node1] which was created previously! 
    ## otherwise recursion won't stop! 
    elif node in visited.keys():
        return visited[node]

    neighbors = []
    
    new_node = Node(node.val, neighbors)

    visited[node] = new_node

    for i in range(len(node.neighbors)):
        neighbor_node = clone_helper(node.neighbors[i], visited)
        neighbors.append(neighbor_node)

    return new_node

def clone(node):
    return clone_helper(node, dict())


node = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])

node.neighbors.append(node2)
node.neighbors.append(node4)
node2.neighbors.append(node)
node2.neighbors.append(node3)
node3.neighbors.append(node2)
node3.neighbors.append(node4)
node4.neighbors.append(node)
node4.neighbors.append(node3)
b=clone(node)

node2_new,node4_new=[ne for ne in b.neighbors]
[ne.val  for ne in node4_new.neighbors]

[1, 3]



