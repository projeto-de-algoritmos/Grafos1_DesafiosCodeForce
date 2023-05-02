def kosaraju(graph):
    def dfs(v, visited, stack):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(v)

    def reverse(graph):
        reversed_graph = {v: [] for v in graph}
        for v in graph:
            for neighbor in graph[v]:
                reversed_graph[neighbor].append(v)
        return reversed_graph

    def dfs_scc(v, visited, scc):
        visited.add(v)
        scc.add(v)
        for neighbor in reversed_graph[v]:
            if neighbor not in visited:
                dfs_scc(neighbor, visited, scc)

    visited = set()
    stack = []
    for v in graph:
        if v not in visited:
            dfs(v, visited, stack)

    reversed_graph = reverse(graph)

    visited = set()
    sccs = []
    while stack:
        v = stack.pop()
        if v not in visited:
            scc = set()
            dfs_scc(v, visited, scc)
            sccs.append(scc)

    return len(sccs) == 1

n, m = map(int, input().split())
street = input()
avenue = input()

graph = {i * m + j: [] for i in range(n) for j in range(m)}

for i in range(n):
    for j in range(m - 1):
        u = i * m + j
        v = u + 1
        if street[i] == '<':
            u, v = v, u
        graph[u].append(v)

for i in range(n - 1):
    for j in range(m):
        u = i * m + j
        v = u + m
        if avenue[j] == '^':
            u, v = v, u
        graph[u].append(v)

if kosaraju(graph):
    print("YES")
else:
    print("NO")
