import sys

input = sys.stdin.readline

vertices = int(input())

array = [[] for i in range(vertices)]

for i in range(len(array)):
    for j in range(len(array)):
        array[i].append(0)


for i in range(vertices):
    store = list(map(int, input().split()))
    for j in range(1, len(store)):
        array[i][store[j]] = 1

for i in array:
    print(*i)
        