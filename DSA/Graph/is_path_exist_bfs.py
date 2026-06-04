from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        neigh=[[] for _ in range(n)]
        
        for n1, n2 in edges:
            neigh[n1].append(n2)
            neigh[n2].append(n1)
            
        q = deque()
        q.append(source)
        seen = set()
        seen.add(source)
        
        while q:
            node = q.popleft()
            if node == destination:
                return True
            for n in neigh[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
                    
        return False