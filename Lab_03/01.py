import sys
input = sys.stdin.readline
def merge(a,b):
    inversions = 0
    i,j = 0,0
    c = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])            
            j += 1
            inversions += len(a) - i
        else:
            c.append(a[i])
            i += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c, inversions

def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)//2
    a1, left = mergesort(arr[:mid])
    a2, right = mergesort(arr[mid:])
    print(a1, a2)
    result, inversion = merge(a1,a2)
    print(result)
    return result, left + right + inversion

    
length = int(input())

array = list(map(int, input().split()))

result, inversions = mergesort(array)

print(inversions)
print(*result)