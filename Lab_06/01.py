import sys
from collections import deque
input = sys.stdin.readline

def Kahn(adjacency_list, vertices, indegree):
       
    queue = deque(u for u in range(1, vertices + 1) if indegree[u] == 0)
    sequence = []
    while queue:
        u = queue.popleft()
        sequence.append(u)
        for i in adjacency_list[u]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    if len(sequence) != vertices:
        return None
    return sequence
    
courses, requirements = map(int, input().split())

adjacency_list = [[] for _ in range(courses + 1)]

indegree = [0 for _ in range(courses + 1)]
path = []

for _ in range(requirements):
    inbound, outbound = map(int, input().split())
    indegree[outbound] += 1
    if not path:
        path.append(inbound)
    elif outbound == path[0]:
        path[0] = inbound
    adjacency_list[inbound].append(outbound)
    
ans = Kahn(adjacency_list, courses, indegree)

if ans:
    print(*ans)

else:
    print(-1)
    