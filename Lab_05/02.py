import sys 
from bisect import insort

sys.setrecursionlimit(2*100000+5)

input = sys.stdin.readline

def DFS(adjacency_list, start, visited, dfs = []):
    
    visited[start] = 1
    dfs.append(start + 1)
    for i in adjacency_list[start]:
        if visited[i - 1] != 1:
            DFS(adjacency_list, i-1, visited)
    return dfs


vertices, edges = map(int, input().split())

inbounds = list(map(int, input().split()))

outbounds = list(map(int, input().split()))

adjacency_list = [[] for i in range(vertices)]

for i in range(len(inbounds)):
    insort(adjacency_list[inbounds[i]-1], outbounds[i])
    insort(adjacency_list[outbounds[i]-1], inbounds[i])
visited = [0 for _ in range(vertices)]
print(*DFS(adjacency_list, 0, visited))
