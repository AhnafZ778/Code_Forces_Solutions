import sys

input = sys.stdin.readline

Size = int(input())

count = 0
Given_Array = input()
Array_Splitted = Given_Array.split()

if Size == 1:
    print("YES")
    
else:
    ## Any odd to odd and even to even
    while count + 2 < Size:
        
        Is_Sorted = True
        
        if int(Array_Splitted[count]) > int(Array_Splitted[count+2]):
            Is_Sorted = False
            
        if not Is_Sorted:
            Array_Splitted[count + 2], Array_Splitted[count] = Array_Splitted[count] , Array_Splitted[count + 2]
            
        count += 1
        
    check = True
    
    for i in range(len(Array_Splitted)-1):
        
        if int(Array_Splitted[i]) > int(Array_Splitted[i + 1]):
            check = False
            break

    if check:
        print("YES")
        
    else:
        print("NO")