<<<<<<< HEAD
from typing import List
class Solution:
    
    def validPath(self, n: int, edges: List[List[int]]):
        
        neighbor=[[] for _ in range(n)]
        
        for u, v in edges:
            neighbor[u].append(v)
            neighbor[v].append(u)
        print('adjacency matrix')
        
        for i in range(n):
            print(f"{i} -> {neighbor[i]}")

class Main:
        def __init__(self):
                self.edges=[[0,1],[1,2],[2,3]]
                obj2=Solution()
                obj2.validPath(4,self.edges)

obj=Main()



        


=======
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbor = defaultdict(list)
        for u, v in edges:
            neighbor[u].append(v)
            neighbor[v].append(u)
>>>>>>> e649026af7bb8d1e9a65ef1bcb4088db857ae85f
