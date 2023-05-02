from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * n
colors = [0] * n
vb = []
vr = []
is_bipartite = True

def bfs(pos):
    global is_bipartite
    visited[pos] = True
    colors[pos] = 1 
    q = deque([pos])
    while q:
        x = q.popleft()
        if colors[x] == 1:
            vb.append(x+1)
        else:
            vr.append(x+1)
        for i in graph[x]:
            next = i
            if colors[next] != 0 and colors[next] == colors[x]:
                is_bipartite = False
                return
            if not visited[next]:
                visited[next] = True
                if colors[x] == 1:
                    colors[next] = 2  
                else:
                    colors[next] = 1  
                q.append(next)

for i in range(n):
    if not visited[i]:
        if not graph[i]:
            continue
        is_bipartite = True
        bfs(i)
        if not is_bipartite:
            print(-1)
            exit()

if is_bipartite:
    s1 = len(vb)
    print(s1)
    print(*vb)
    s2 = len(vr)
    print(s2)
    print(*vr)
else:
    print(-1)
