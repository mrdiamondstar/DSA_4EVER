from collections import deque
from typing import List
class Solution:
    def dag(graph :  List[List[int]], n : int ):

        inorder =[0] *n

        #find inorder of without and no depedecy which has 0 indegree
        for u in range(n):
            for v in graph[u]:
                inorder[v] += 1

        queue=deque() 
        
        
        for i in range(len(inorder)):
            if inorder[i] ==0:
                queue.append(i)   
                
        topological_order=[]        
        
        while queue:
            node=queue.popleft()
            topological_order.append(node)

            
            for nieghbor in graph[node]:
                inorder[nieghbor] -= 1
                
                if inorder[nieghbor]== 0:
                    queue.append(nieghbor)
                    
                    
        #to detect cycle  
        if len(topological_order) != n:
            return []
        
        return topological_order