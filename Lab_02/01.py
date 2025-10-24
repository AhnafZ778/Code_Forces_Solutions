import sys

input = sys.stdin.readline

length , target = input().split(" ")

length = int(length)
target = int(target)
array = input().split(" ")

left = 0
right = int(length)-1

found = False
while left < right:
    total = int(array[left]) + int(array[right])
    if total > target:
        right -= 1
    elif total < target:
        left += 1
    else:
        found = True
        break
if found:
    print(left + 1, right + 1)
else:
    print(-1)
