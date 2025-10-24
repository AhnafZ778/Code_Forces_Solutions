import sys

input = sys.stdin.readline

array_size, target = list(map(int, input().split(" ")))

array = list(map(int, input().split(" ")))

new_array = []

for i in range(array_size):
    new_array.append((array[i], i))
    
new_array.sort()
found = False
if array_size < 4:
    add = sum(array)
    if add == target:
        for i in range(len(array)):
            print(i + 1, end = " ")
    else:
        print(-1)
else:
    for i,a in enumerate(new_array):
        left = i + 1
        right = array_size - 1
        while left < right:
            if a[0] + new_array[left][0] + new_array[right][0] > target:
                right -= 1
            elif a[0] + new_array[left][0] + new_array[right][0] < target:
                left += 1
            else:
                found = True
                break
        if found:
            break
    if found:
        print(new_array[i][1] + 1, new_array[left][1] + 1, new_array[right][1] + 1)
    else:
        print(-1)