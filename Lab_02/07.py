import sys

def lower_bound(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
    
    
def upper_bound(array, target):
    left, right = 0, len(array)
    while left < right:
        mid = (left + right) // 2
        if array[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

input = sys.stdin.readline

array_size, queries = map(int, input().split())
array = list(map(int, input().split()))
result = []
for _ in range(queries):
    lower, upper = map(int, input().split())
    left = lower_bound(array, lower)
    right = upper_bound(array, upper)
    result.append(right - left)

for i in result:
    print(i)