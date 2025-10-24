import sys
from collections import deque

def bfs(start, adjacency_list, vertices):
    queue = deque()
    queue.append(start)
    distance = [-1 for i in range(vertices+1)]
    distance[start] = 0
    while queue:
        u = queue.popleft()
        for i in adjacency_list[u]:
            if distance[i] == -1:
                distance[i] = distance[u]+1
                queue.append(i)
    return distance
    


input = sys.stdin.readline

vertices,edges,source,destination = map(int, input().split())
inbound = list(map(int, input().split()))
outbound = list(map(int, input().split()))

adjacency_list = [[] for i in range(vertices+1)]

for i in range(len(inbound)):
    adjacency_list[inbound[i]].append(outbound[i])
    adjacency_list[outbound[i]].append(inbound[i])

for i in adjacency_list:
    i.sort()

distS = bfs(source, adjacency_list, vertices)
if distS[destination] == -1:
    print(-1)
else:
    
    distD = bfs(destination, adjacency_list, vertices)

    path = [source]
    cur = source
    for _ in range(distS[destination]):
        candidates = [v for v in adjacency_list[cur]
        if distS[v] == distS[cur] + 1 and distS[v] + distD[v] == distS[destination]]
        cur = candidates[0]
        path.append(cur)

    print(distS[destination])
    print(*path)
    