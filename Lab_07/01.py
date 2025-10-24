import sys
import heapq

input = sys.stdin.readline

vertices, edges, source, destination = map(int, input().split())

inbound = list(map(int, input().split()))
outbound = list(map(int, input().split()))
weights = list(map(int, input().split()))

adjacency_list = [[] for _ in range(vertices + 1)]

for i in range(len(inbound)):
    adjacency_list[inbound[i]].append((outbound[i], weights[i]))

distance = [float("inf") for _ in range(vertices + 1)]
distance[source] = 0
heap = [(0, source)]

parent = [-1 for _ in range(vertices + 1)]

while heap:
    
    dist, node = heapq.heappop(heap)
    if node == destination:
        break
    for next_node, weight in adjacency_list[node]:
        new_distance = dist + weight
        if new_distance < distance[next_node]:
            distance[next_node] = new_distance
            parent[next_node] = node
            heapq.heappush(heap, (new_distance, next_node))
            
if distance[destination] == float("inf"):
    print(-1)
    exit()

path = []
current = destination

while current != -1:
    path.append(current)
    current = parent[current]

path.reverse()

print(distance[destination])
print(*path)
        