import sys

input = sys.stdin.readline

edges, vertices = map(int, input().split())

start = list(map(int, input().split()))

end = list(map(int, input().split()))

difference = [0] * edges

for i in range(len(start)):
    difference[start[i] - 1] -= 1
    difference[end[i] - 1] += 1
    
print(*difference)
