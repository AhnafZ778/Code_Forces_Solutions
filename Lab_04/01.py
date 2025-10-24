import sys

input = sys.stdin.readline

array_size, edges = map(int, input().split())

array = [[]for i in range(array_size)]

for i in range(len(array)):
    for j in range(len(array)):
        array[i].append(0)
for i in range(edges):
    row, col, weight = map(int, input().split()) 
    array[row - 1][col - 1] = weight

for i in array:
    print(*i)

