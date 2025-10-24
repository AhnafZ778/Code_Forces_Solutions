import sys
from collections import deque

input = sys.stdin.readline

def kahn_cycle_detector(vertices, adjacency_list):
    
    indegree = [0 for _ in range(vertices + 1)]
    for i in range(1, vertices + 1):
        for j in adjacency_list[i]:
            indegree[j] += 1
            
    queue = deque([u for u in range(1, vertices + 1) if indegree[u] == 0])
    
    visits = 0
    while queue:
        u = queue.popleft()
        visits += 1
        for i in adjacency_list[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    return visits < vertices



vertices, edges = map(int, input().split())

adjacency_list = [[] for _ in range(vertices + 1)]

for _ in range(edges):
    inbound, outbound = map(int, input().split())
    adjacency_list[inbound].append(outbound)
    
answer = kahn_cycle_detector(vertices, adjacency_list)

if answer:
    print("YES")
else:
    print("NO")