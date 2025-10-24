import sys
import heapq

input = sys.stdin.readline

vertices, edges, source, destination = map(int, input().split())

adjacency_list = [[] for _ in range(vertices + 1)]
for _ in range(edges):
    u, v, w = map(int, input().split())
    adjacency_list[u].append((v, w))
    adjacency_list[v].append((u, w))

INF = float("inf")


first_distance = [INF] * (vertices + 1)
second_distance = [INF] * (vertices + 1)

first_distance[source] = 0


heap = [(0, source)]

while heap:
    dist, node = heapq.heappop(heap)


    if dist > second_distance[node]:
        continue

    for next_node, weight in adjacency_list[node]:
        new_distance = dist + weight


        if new_distance < first_distance[next_node]:

            second_distance[next_node] = first_distance[next_node]
            first_distance[next_node] = new_distance
            heapq.heappush(heap, (new_distance, next_node))

        elif first_distance[next_node] < new_distance < second_distance[next_node]:
            second_distance[next_node] = new_distance
            heapq.heappush(heap, (new_distance, next_node))

answer = second_distance[destination]

if answer == INF:
    print(-1)
else:
    print(answer)