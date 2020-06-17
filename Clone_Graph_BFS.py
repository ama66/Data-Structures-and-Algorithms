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

def clone(node):
    
    queue = []

    visited = {}

    queue.append(node)

    while len(queue) > 0:
        
        cur = queue.pop(0)

        new_node = None
        
       # if current node was visitied we must have created a clone of it so 
        ## we retrieve it and call it new_node otherwise we create it from scratch by calling Node class
        if cur in visited.keys():
            new_node = visited[cur]
        else:
             ## if this clone is newly created we need to update the visited dictionary
            new_node = Node(cur.val, [])
            visited[cur] = new_node
        
        ## Neighbors of the clone of current node
        neighbors = new_node.neighbors
    
        # now iterate over current node neighors
        for i in range(len(cur.neighbors)):
            ## if for some of the neighbors we have already created clones 
            ## then we append them to the neighbors of the new clone (new_node.neighbors or neighbors)
            if cur.neighbors[i] in visited.keys():
                neighbors.append(visited[cur.neighbors[i]])
            else:
                ## otherwise we append neighbors to the queue
                queue.append(cur.neighbors[i])
                ## and we clone the neighbors and append to the new clone neighbors 
                ## and mark them as in the visited dictionary
                new_neighbor_node = Node(cur.neighbors[i].val, [])
                neighbors.append(new_neighbor_node)
                visited[cur.neighbors[i]] = new_neighbor_node

    return visited[node]




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

[ne.val  for ne in node4_new.neighbors]

[1, 3]
