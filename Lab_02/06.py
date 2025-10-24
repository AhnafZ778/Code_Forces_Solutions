import sys
from collections import defaultdict

input = sys.stdin.readline

array_size, limit = list(map(int, input().split(" "))) 

array = list(map(int, input().split(" ")))

left = 0
result = 0

distinct = defaultdict(int)
for right in range(len(array)):
    distinct[array[right]] += 1
    while len(distinct) > limit and left <= right:
        distinct[array[left]] -= 1
        if distinct[array[left]] == 0:
            del distinct[array[left]]
        left += 1
    subarray_length = right - left + 1
    result = max(result, subarray_length)

print(result)