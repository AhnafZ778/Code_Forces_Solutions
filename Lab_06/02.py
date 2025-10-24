import sys
from collections import deque

input = sys.stdin.readline

players, tackles = map(int, input().split())

adjacency_list = [[] for _ in range(players + 1)]

for _ in range(tackles):
    tackler, tackled = map(int, input().split())
    adjacency_list[tackler].append(tackled)
    adjacency_list[tackled].append(tackler)
    
color = [-1 for _ in range(players + 1)]

answer = 0

for i in range(1, players + 1):
    
    if color[i] != -1:
        continue
    if not adjacency_list[i]:
        answer += 1
        continue
    queue = deque()
    queue.append(i)
    color[i] = 0
    player_count, robot_count = 1, 0
    while queue: 
        u = queue.popleft()
        for v in adjacency_list[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                if color[v] == 0:
                    player_count += 1
                else:
                    robot_count += 1
                queue.append(v)
                
    answer += max(player_count, robot_count)

print(answer)
    
    