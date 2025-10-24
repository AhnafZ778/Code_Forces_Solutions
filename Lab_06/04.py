import sys
from collections import deque


input = sys.stdin.readline

def bfs(adjacency_list, vertices, start):
    
    distance = [-1 for _ in range(vertices + 1)]
    max_dist = 0
    index = start
    queue = deque()
    queue.append(start)
    distance[start] = 0
    while queue:
        u = queue.popleft()
        for i in adjacency_list[u]:
            if distance[i] == -1:
                distance[i] = distance[u] + 1
                queue.append(i)
            if distance[i] > max_dist:
                index = i
                max_dist = max(max_dist, distance[i])
    return index, max_dist
                

nodes = int(input())

adjacency_list = [[] for _ in range(nodes + 1)]

for _ in range(nodes - 1):
    inbound, outbound = map(int, input().split())
    adjacency_list[inbound].append(outbound)
    adjacency_list[outbound].append(inbound)

index_1, max_1 = bfs(adjacency_list, nodes, 1)
index_2, max_2 = bfs(adjacency_list, nodes, index_1)

print(max_2)
print(index_1, index_2)

