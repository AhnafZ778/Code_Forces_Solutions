import sys

input = sys.stdin.readline

vertices, edges = map(int, input().split())

array = [[] for i in range(vertices)]

start = list(map(int, input().split()))
end = list(map(int, input().split()))
weight = list(map(int, input().split()))

for i in range(edges):
    array[start[i]-1].append((end[i],weight[i]))

for i in range(len(array)):
    print(f"{i+1}:", *array[i])

