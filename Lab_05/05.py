import sys
from collections import deque

input = sys.stdin.readline

nodes, root = map(int, input().split())

adjacency_list = [[] for _ in range(nodes+1)]

for _ in range(1, nodes):
    inbound_edge, outbound_edge = map(int, input().split())
    adjacency_list[inbound_edge].append(outbound_edge)
    adjacency_list[outbound_edge].append(inbound_edge)

parent = [0] * (nodes+1)
queue = deque()
order = []
queue.append(root)
parent[root] = -1

while queue:
    u = queue.popleft()
    order.append(u)
    for i in adjacency_list[u]:
        if i != parent[u]:
            parent[i] = u
            queue.append(i)

subtree = [0] * (nodes + 1)
order.reverse()

for i in order:
    size = 1
    for j in adjacency_list[i]:
        if j != parent[i]:
            size += subtree[j]
    subtree[i] = size
    
answers = []

queries = int(input())

for _ in range(queries):
    q = int(input())
    answers.append(subtree[q])

for i in answers:
    print(i)

