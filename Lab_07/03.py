import sys
from heapq import heappop, heappush

input = sys.stdin.readline

cities, roads = map(int, input().split())

adjacency_list = [[] for _ in range(cities + 1)]

for _ in range(roads):
    inbound, outbound, weight = map(int, input().split())
    adjacency_list[inbound].append((outbound, weight))
    adjacency_list[outbound].append((inbound, weight))
danger = [float("inf") for _ in range(cities + 1)]
danger[1] = 0
heap = [(0,1)]

while heap:
    weight, node = heappop(heap)
    for next_node, new_weight in adjacency_list[node]:
        new_danger = max(weight, new_weight)
        if danger[next_node] > new_danger:
            danger[next_node] = new_danger
            heappush(heap, (new_danger, next_node))

for i in range(1, cities + 1):
    if danger[i] != float("inf"):
        print(danger[i], end = " ")
    else:
        print(-1, end = " ")