import sys

input = sys.stdin.readline

a_size, b_size, target = list(map(int, input().split(" ")))

first_line = list(map(int, input().split(" ")))
second_line = list(map(int, input().split(" ")))

pair = [0, 0]
left = 0
right = len(second_line)-1
minimum = float("inf")

while left < len(first_line) and right > -1:
    difference = abs(first_line[left] + second_line[right] - target)
    sum = first_line[left] + second_line[right]
    if difference == 0:
        pair[0], pair[1] = left, right
        break
    if difference < minimum:
        minimum = difference
        pair[0], pair[1] = left, right
    if sum > target:
        right -= 1
    elif sum < target:
        left += 1

print(pair[0]+1 , pair[1]+1)