# 2606

from collections import defaultdict

m = int(input())
n = int(input())

graph = defaultdict(list)

for i in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

graph = dict(graph)

cnt = set()

def searchConta(n):
    global cnt

    if n not in graph:
        return
    
    if (graph[n] == []):
        return

    arr = graph[n]
    graph[n] = []

    for i in arr:
        graph[i].remove(n)
    for i in arr:
        cnt.add(i)
        searchConta(i)

    return

searchConta(1)
print(len(cnt))