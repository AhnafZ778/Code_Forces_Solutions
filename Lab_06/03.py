import sys
from collections import deque
input = sys.stdin.readline

def minimum_moves(N, x1, y1, x2, y2):
    
    visited = [0] * (N*N)
    
    possible_moves = ((2,1), (1,2), (-1, 2), (-2, 1),(-2,-1),(-1, -2), (1, -2), (2, -1))
    
    x1 -=1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    queue = deque()
    queue.append((x1,y1))
    visited[x1*N + y1] = 1
    end = x2*N + y2
    moves = 0
    
    while queue:
        
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for mx,my in possible_moves:
                new_x, new_y = x + mx, y + my
                if 0 <= new_x < N and 0 <= new_y < N:
                    current = new_x*N + new_y
                    if visited[current]:
                        continue
                    if current == end:
                        return moves + 1
                    visited[current] = 1
                    queue.append((new_x, new_y))
        moves += 1
        
    return -1  
        


size = int(input())

x1,y1,x2,y2 = map(int, input().split())

print(minimum_moves(size, x1, y1, x2, y2))