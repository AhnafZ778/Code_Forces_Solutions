import sys
from collections import deque

input = sys.stdin.readline

def visit(adjacency_list, vertices):
    visited = [0 for _ in range(vertices + 1)]
    queue = deque()
    queue.append(1)
    visited[1] = 1
    flag = False
    while queue:
        u = queue.popleft()
        for i in adjacency_list[u]:
            if visited[i] == 0:
                visited[i] += 1
                queue.append(i)
            else:
                flag = True
                break
        if flag:
            break
        
    return flag
    


vertices, edges = map(int, input().split())

adjacency_list = [[] for _ in range(vertices + 1)]
for _ in range(edges):
    inbound, outbound = map(int, input().split())
    adjacency_list[inbound].append(outbound)
    
answer = visit(adjacency_list, vertices)

if answer:
    print("YES")
else:
    print("NO")