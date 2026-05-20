class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbor = defaultdict(list)
        for u, v in edges:
            neighbor[u].append(v)
            neighbor[v].append(u)
