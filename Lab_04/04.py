import sys

input = sys.stdin.readline

vertices, edges = map(int, input().split())

start = list(map(int, input().split()))

end = list(map(int, input().split()))

edge = [0] * (vertices)

for i in range(len(start)):
    edge[start[i] - 1] += 1
    edge[end[i] - 1] += 1
    
count = 0
for i in edge:
    if i % 2 != 0:
        count += 1

if count == 0 or count == 2:
    print("YES")
else:
    print("NO")