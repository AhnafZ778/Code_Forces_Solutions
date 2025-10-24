import sys 
from collections import deque
from bisect import insort 
input = sys.stdin.readline

vertices, edges = map(int, input().split())
 
adjacency_matrix = [[] for i in range(vertices)]
 
for _ in range(edges):
    edge_1, edge_2 = map(int, input().split())
    insort(adjacency_matrix[edge_1 - 1], edge_2)
    insort(adjacency_matrix[edge_2 - 1], edge_1)
    
visited = [0 for _ in range(vertices)]
 
queue = deque()
 
queue.append(0)
visited[0] = 1
BFS = []
while queue:
    u = queue.popleft()
    for i in adjacency_matrix[u]:
        if visited[i-1] != 1:
            queue.append(i-1)
            visited[i-1] = 1
    BFS.append(u + 1)     
 
print(*BFS)
