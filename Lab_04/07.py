import sys
input = sys.stdin.readline

rows, columns, knights = map(int, input().split())

positions = {}

for i in range(knights):
    position = tuple(map(int, input().split()))
    positions[position] = i

flag = True
for i in positions.keys():
    move_1 = (i[0] - 2, i[1] - 1)
    move_2 = (i[0] - 2, i[1] + 1)
    move_3 = (i[0] - 1, i[1] - 2)
    move_4 = (i[0] - 1, i[1] + 2)
    move_5 = (i[0] + 1, i[1] - 2)
    move_6 = (i[0] + 1, i[1] + 2)
    move_7 = (i[0] + 2, i[1] - 1)
    move_8 = (i[0] + 2, i[1] + 1)
    if move_1 in positions:
        flag = False
        break
    if move_2 in positions:
        flag = False
        break
    if move_3 in positions:
        flag = False
        break
    if move_4 in positions:
        flag = False
        break
    if move_5 in positions:
        flag = False
        break
    if move_6 in positions:
        flag = False
        break
    if move_7 in positions:
        flag = False
        break
    if move_8 in positions:
        flag = False
        break
    
if flag:
    print("NO")
else:
    print("YES")
    
    
        






    