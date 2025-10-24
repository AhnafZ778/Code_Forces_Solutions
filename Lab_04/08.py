import sys

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N, Q = map(int, input().split())

array = []

for i in range(1, N+1):
    store = []
    for j in range(1, N+1):
        if gcd(i,j) == 1 and i != j:
            store.append(j)
    array.append(store)
ans = []
for i in range(Q):
    node, kth = map(int, input().split())
    if kth > len(array[node - 1]):
        ans.append(-1)
        continue
    ans.append(array[node - 1][kth - 1])

for i in ans:
    print(i)


            
