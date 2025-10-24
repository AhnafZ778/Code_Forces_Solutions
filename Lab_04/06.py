import sys

input = sys.stdin.readline

size = int(input())

position = list(map(int, input().split()))

up = [position[0], position[1] - 1]
down = [position[0], position[1] + 1]
left = [position[0] - 1, position[1]]
right = [position[0] + 1, position[1]]
up_left = [position[0] - 1, position[1] - 1]
up_right = [position[0] + 1, position[1] - 1]
down_left = [position[0] -1, position[1] + 1]
down_right = [position[0] + 1, position[1] + 1]

count = 0
store = []
if up_left[0] > 0 and up_left[1] > 0:
    count += 1
    store.append(up_left)
if left[0] > 0:
    count += 1
    store.append(left)
if down_left[0] > 0 and down_left[1] <= size:
    count += 1
    store.append(down_left)
if up[1] > 0:
    count += 1
    store.append(up)
if down[1] <= size:
    count += 1
    store.append(down)
if up_right[0] <= size and up_right[1] > 0:
    count += 1
    store.append(up_right)
if right[0] <= size:
    count += 1
    store.append(right)
if down_right[0] <= size and down_right[1] <= size :
    count += 1
    store.append(down_right)
    
print(count)
for i in store:
    print(*i)
     