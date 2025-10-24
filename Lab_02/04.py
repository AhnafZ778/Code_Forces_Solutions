import sys
import time

start = time.time()
input = sys.stdin.readline

first_size = int(input())

first_arr = list(map(int, input().split(" ")))

second_size = int(input())

second_arr = list(map(int, input().split(" ")))

count_first = 0
count_second = 0
new_arr = []
while count_first < first_size and count_second < second_size:
    if first_arr[count_first] < second_arr[count_second]:
        new_arr.append(first_arr[count_first])
        count_first += 1
    elif first_arr[count_first] > second_arr[count_second]:
        new_arr.append(second_arr[count_second])
        count_second += 1
    else:
        new_arr.append(first_arr[count_first])
        count_first += 1

new_arr.extend(first_arr[count_first:])
new_arr.extend(second_arr[count_second:])

print(*new_arr)
print(time.time() - start)