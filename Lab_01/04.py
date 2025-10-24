import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    arr = input()
    new_arr = arr.split()
    check = True
    count = 0
    while check and count < len(new_arr) - 1:
        if not int(new_arr[count + 1]) >= int(new_arr[count]):
            check = False
            break
        count += 1
    if check:
        print("YES")
    else:
        print("NO")
            
        
        
# a = "1 2 3 4 5 100"
# b = (a.split())
# print(b)