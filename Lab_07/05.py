import sys
import heapq

input = sys.stdin.readline

vertices, edges = map(int, input().split())

inbound = list(map(int, input().split()))
outbound = list(map(int, input().split()))
weights = list(map(int, input().split()))

adjacency_list = [[] for _ in range(vertices + 1)]

for i in range(edges):
    adjacency_list[inbound[i]].append((outbound[i], weights[i]))
    
distances = [[float("inf"), float("inf")] for _ in range(vertices + 1)]

heap = []

for node, weight in adjacency_list[1]:
    parity = weight & 1
    if weight < distances[node][parity]:
        distances[node][parity] = weight
        heapq.heappush(heap, (weight, node, parity))

while heap:
    
    distance, node, parity = heapq.heappop(heap)
    
    if node == vertices:
        print(distance)
        exit()
    for next_node, next_weight in adjacency_list[node]:
        new_parity = next_weight & 1
        
        new_distance = distance + next_weight
        
        if new_distance < distances[next_node][new_parity]:
            distances[next_node][new_parity] = new_distance
            heapq.heappush(heap, (new_distance, next_node, new_parity))
            
answer = min(distances[vertices])

if answer == float("inf"):
    print(-1)
else:
    print(answer)