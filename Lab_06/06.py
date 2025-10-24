import sys
from collections import deque

input = sys.stdin.readline
    
nodes, edges, source_nodes, destination_nodes = map(int, input().split())

adjacency_list = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    inbound, outbound = map(int,input().split())
    adjacency_list[inbound].append(outbound)
    adjacency_list[outbound].append(inbound)
    
sources = list(map(int, input().split()))
destinations = list(map(int, input().split()))

distance = [-1 for _ in range(nodes + 1)]

queue = deque()

for i in sources:
    if distance[i] == -1:
        distance[i] = 0
        queue.append(i)
        
while queue:
    
    u = queue.popleft()
    for i in adjacency_list[u]:
        if distance[i] == -1:
            distance[i] = distance[u] + 1
            queue.append(i)
    
output = []

for i in destinations:
    output.append(str(distance[i]))
    
print(*output)