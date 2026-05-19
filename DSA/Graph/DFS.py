graph = {
    0:[1,2],
    1:[0,3,4],
    2:[0],
    3:[1],
    4:[1]
}

visited = set()

def dfs(node):

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor)

dfs(0)