import sys
import heapq

input = sys.stdin.readline

vertices, edges, source, destination = map(int, input().split())

weights = [0] + list(map(int, input().split()))

adjacency_list = [[] for _ in range(vertices + 1)]


for i in range(edges):
    inbound, outbound = map(int, input().split())
    adjacency_list[inbound].append(outbound)
    
distances = [float("inf") for _ in range(vertices + 1)]
distances[source] = weights[source]

heap = [(distances[source], source)]

while heap:
    
    dist, node = heapq.heappop(heap)
    if node == destination:
        break
    for next_node in adjacency_list[node]:
        new_distance = dist + weights[next_node]
        if new_distance < distances[next_node]:
            distances[next_node] = new_distance
            heapq.heappush(heap, (new_distance, next_node))
            
if distances[destination] == float("inf"):
    print(-1)
else:
    print(distances[destination])
    
    