import sys
from collections import defaultdict

def dfs(v, t, f, r):
    if v == t:
        return r
    visited[v] = True
    for u, w in graph[v]:
        if not visited[u]:
            res = dfs(u, t, -f, r * w * f)
            if res != 0:
                return res
    return 0

N = int(input())
gears = [list(map(int, input().split())) for _ in range(N)]
graph = defaultdict(list)
for i in range(N):
    for j in range(i+1, N):
        xi, yi, ri = gears[i]
        xj, yj, rj = gears[j]
        if (xi-xj)**2 + (yi-yj)**2 == (ri+rj)**2:
            graph[i+1].append((j+1, ri/rj))
            graph[j+1].append((i+1, rj/ri))
visited = [False] * (N+1)
res = dfs(1, N, 1, 1)
if res == 0:
    print("Could Not Process")
else:
    print("{:.2f}".format(abs(res) if res < 0 else res))
