import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    print(int((N*(N+1))/2))
