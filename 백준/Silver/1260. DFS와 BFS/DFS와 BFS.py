# 1260
from collections import deque

# input
n, m, v = map(int, input().split())
graph = {key : [] for key in range(1, n + 1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# dfs
sequence = []   
visited = [False] * (n + 1)

def dfs(n):
    global sequence

    if visited[n]:
        return
    
    sequence.append(n)
    visited[n] = True

    for node in sorted(graph[n]):
        if not visited[node]:
            dfs(node)
    return sequence
    
print(*dfs(v))

# bfs
def bfs(start):
    sequence = []
    visited = [False] * (n + 1)
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if visited[x]:
            continue
        sequence.append(x)
        visited[x] = True
        for node in sorted(graph[x]):
            if not visited[node]:
                queue.append(node)
    return sequence

print(*bfs(v))
