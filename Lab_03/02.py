import sys
from bisect import bisect_right, insort

input = sys.stdin.readline

array_size = int(input())
array = list(map(int, input().split()))
result = 0

sorted_left = []

for i in range(array_size):
    threshold = array[i] ** 2
    index = bisect_right(sorted_left, threshold)
    result += len(sorted_left) - index
    insort(sorted_left, array[i])


print(result)