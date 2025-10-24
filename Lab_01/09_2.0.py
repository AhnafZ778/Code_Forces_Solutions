import sys

input = sys.stdin.readline

total_departures = int(input())
train_list = []

for i in range(total_departures):
    departure = input().split()
    train_name = departure[0]
    destination = departure[len(departure)-3]
    time = departure[len(departure)-1]
    train_list.append((train_name, time, destination, i))
    
for i in range(total_departures - 1):
    for j in range(i + 1 , total_departures):
        if train_list[j][0] < train_list[i][0]:
            train_list[i], train_list[j] = train_list[j], train_list[i]
        elif train_list[j][0] == train_list[i][0]:
            hour_1, minute_1 = train_list[i][1].split(":")
            hour_2, minute_2 = train_list[j][1].split(":")
            time_1 = int(hour_1)*60 + int(minute_1)
            time_2 = int(hour_2)*60 + int(minute_2)
            if time_2 > time_1:
                train_list[i], train_list[j] = train_list[j], train_list[i]
            else:
                if train_list[j][3] < train_list[i][3]:
                    train_list[i], train_list[j] = train_list[j], train_list[i]

for i in range(total_departures):
    print(f"{train_list[i][0]} will departure for {train_list[i][2]} at {train_list[i][1]}")
            
            
            
# ABCD will departure for Mymensingh at 00:30
# DhumketuExpress will departure for Chittagong at 02:30
# ABC will departure for Dhaka at 17:30
# ABCD will departure for Chittagong at 01:00
# ABC will departure for Khulna at 03:00
# ABC will departure for Barisal at 03:00
# ABCE will departure for Sylhet at 23:05
# PadmaExpress will departure for Dhaka at 19:30            
            
            