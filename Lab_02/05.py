import sys

input = sys.stdin.readline

array_size, limit = list(map(int, input().split(" "))) 

array = list(map(int, input().split(" ")))

left = 0
add = 0
result = 0

for right in range(len(array)):
    add += array[right]
    while add > limit and left <= right:
        add-= array[left]
        left += 1
    subarray_length = right - left + 1
    result = max(result, subarray_length)

print(result)