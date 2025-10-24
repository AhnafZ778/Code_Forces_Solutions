import sys
from collections import deque

input = sys.stdin.readline

rows, characters = map(int, input().split())

adjacency_list = [list(input().strip()) for _ in range(rows)]

visited = [[False] * characters for _ in range(rows)]
ans = 0
directions = [(1,0), (0, 1), (-1, 0), (0, -1)]


for i in range(rows):
    for j in range(characters):
        if adjacency_list[i][j] != "#" and not visited[i][j]:
            queue = deque([(i, j)])
            visited[i][j] = True
            diamonds = 0
            while queue:
                x,y = queue.popleft()
                
                if adjacency_list[x][y] == "D":
                    diamonds += 1
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    if 0 <= new_x < rows and 0 <= new_y < characters and not visited[new_x][new_y] and adjacency_list[new_x][new_y] != "#":
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))
            ans = max(ans, diamonds)

print(ans)
                
    