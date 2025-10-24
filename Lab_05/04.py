import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, adjacency_list, vertices):
    queue = deque()
    queue.append(start)
    distance = [-1 for i in range(vertices+1)]
    parent = [0] * (vertices+1)
    distance[start] = 0
    while queue:
        u = queue.popleft()
        for i in adjacency_list[u]:
            if distance[i] == -1:
                distance[i] = distance[u]+1
                parent[i] = u
                queue.append(i)
    return distance, parent

def path_finder(destination, source, parent):
    
    path = []
    cur = destination
    while cur != 0:
        path.append(cur)
        if cur == source:
            break
        cur = parent[cur]
    path.reverse()
    return path



vertices, edges, source, destination, mandatory = map(int, input().split())

adjacency_list = [[] for _ in range(vertices+1)]

for i in range(edges):
    inbound, outbound = map(int, input().split())
    adjacency_list[inbound].append(outbound)
    
distS, parentS = bfs(source, adjacency_list, vertices)
if distS[mandatory] == -1:
    print(-1)
else:
    distM, parentM = bfs(mandatory, adjacency_list, vertices)
    if distM[destination] == -1:
        print(-1)
    else:
        path_S_M= path_finder(mandatory, source, parentS)
        path_M_D = path_finder(destination, mandatory, parentM)
        
        path = path_S_M + path_M_D[1:]
        
        print(len(path)-1)
        print(*path)