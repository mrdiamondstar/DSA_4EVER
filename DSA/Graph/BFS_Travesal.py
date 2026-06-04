from collections import deque
class Solution:
    def __init__(self):
        
        self.graph = { 
            1:[1,2],
            2:[1,3],
            3:[1,4],
            4:[2,],
            5:[3,2]
            }
        
    def bfs(self,first):
        
        visited=set()
        queue=deque([first])
        visited.add(first)
        
        while queue:
            node=queue.popleft()
            print(node , end = " ")
            
            for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        


obj=Solution()
obj.bfs(1)