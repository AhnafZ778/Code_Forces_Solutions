import sys
from heapq import heappop, heappush

def dijkstra(adjacency_list, vertices, start):
    distances = [float("inf") for _ in range(vertices + 1)]
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        distance, node = heappop(heap)
        
        for next_node, weight in adjacency_list[node]:
            new_distance = distance + weight
            if distances[next_node] > new_distance:
                distances[next_node] = new_distance
                heappush(heap, (new_distance, next_node))
    return distances
        


input = sys.stdin.readline

vertices, edges, alice, bob = map(int, input().split())

adjacency_list = [[] for _ in range(vertices + 1)]

for _ in range(edges):
    inbound, outbound, weight = map(int, input().split())
    adjacency_list[inbound].append((outbound, weight))

d_alice = dijkstra(adjacency_list, vertices, alice)
d_bob = dijkstra(adjacency_list, vertices, bob)
meet_time = float("inf")
meet_spot = -1
for i in range(1, vertices + 1):
    if d_alice[i] < float("inf") and d_bob[i] < float("inf"):
        time = max(d_alice[i], d_bob[i])
        if time < meet_time:
            meet_time = time
            meet_spot = i
            
if meet_spot == -1:
    print(-1)
else:
    print(meet_time, meet_spot)