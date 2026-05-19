graph = {
    0:[1,2],
    1:[0,3,4],
    2:[0],
    3:[1],
    4:[1]
}

def dfs(start):

    visited = set()

    stack = [start]

    while stack:

        node = stack.pop()

        if node not in visited:

            visited.add(node)

            print(node, end=" ")

            for neighbor in reversed(graph[node]):

                if neighbor not in visited:
                    stack.append(neighbor)

dfs(0)