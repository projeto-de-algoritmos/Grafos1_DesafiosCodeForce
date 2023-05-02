import sys
    
N, M = map(int, sys.stdin.readline().split())
cnt = [0] * N
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    cnt[min(a, b) - 1] += 1
res = N
for i in range(N):
    if cnt[i] > 0:
        res -= 1
    
Q = int(sys.stdin.readline())
for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        cnt[min(a, b) - 1] += 1
        if cnt[min(a, b) - 1] == 1:
            res -= 1
    elif query[0] == 2:
        a, b = query[1], query[2]
        cnt[min(a, b) - 1] -= 1
        if cnt[min(a, b) - 1] == 0:
            res += 1
    else:
        print(res)