def cycle(graph,current_node, parent_node,visited):
    visited.add(current_node)
    
    for node in graph[current_node]:
        if node not in visited:
            cycle(graph,node,current_node,visited)

        elif node != parent_node:
            return True
    return False
        
        
#we pass (graph,0,-1,visited)

#at starting parent node is -1