import sys

input = sys.stdin.readline

total_departures = int(input())
train_list = []

for i in range(total_departures):
    departure = input().split()
    train_name = departure[0]
    destination = departure[4]
    time = departure[6]
    train_list.append((train_name, time, destination, i))
    
for i in range(total_departures - 1):
    index = i
    for j in range(i + 1, total_departures):
        if train_list[j][0] < train_list[index][0]:
            index = j
        elif train_list[j][0] == train_list[index][0]:
            hour_j, minutes_j = train_list[j][1].split(":")
            hour_index, minutes_index = train_list[index][1].split(":")
            sum_index = int(hour_index)*60 + int(minutes_index)
            sum_j = int(hour_j)*60 + int(minutes_j)
            if sum_j > sum_index:
                index = j
            elif sum_j == sum_index:
                if train_list[j][3] < train_list[index][3]:
                    idx = j
                
    if index != i:
        train_list[i], train_list[index] = train_list[index], train_list[i]
        
for train in train_list:
    print(f"{train[0]} will departure for {train[2]} at {train[1]}")

            
# ABCD will departure for Mymensingh at 00:30
# DhumketuExpress will departure for Chittagong at 02:30
# ABC will departure for Dhaka at 17:30
# ABCD will departure for Chittagong at 01:00
# ABC will departure for Khulna at 03:00
# ABC will departure for Barisal at 03:00
# ABCE will departure for Sylhet at 23:05
# PadmaExpress will departure for Dhaka at 19:30