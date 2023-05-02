N = 200100

vis = [False]*N
adj = [[] for i in range(N)]
st = []

def dfs(s):
    vis[s]=True
    stack = [s]
    while stack:
        u = stack.pop()
        st.append(u)
        for e in adj[u]:
            if not vis[e]:
                vis[e] = True
                stack.append(e)

n, m = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

cnt = 0

for i in range(1,n+1):
    if not vis[i]:
        dfs(i)

    k=1
    if len(st)>2:
        while st:
            if len(adj[st[-1]])!=2:
                k=0
                break

            st.pop()

        if k:
            cnt+=1

    st.clear()

print(cnt)
