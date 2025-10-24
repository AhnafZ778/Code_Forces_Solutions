import sys

input = sys.stdin.readline

size = int(input())

Given_Array = input()

Array = Given_Array.split()

if size == 1:
    print("YES")
else:
    for i in range(size-1):
        for j in range(i + 2, size, 2):
            if int(Array[i]) > int(Array[j]):
                Array[i], Array[j] = Array[j], Array[i]

    check = True
    for i in range(size - 1):
        if int(Array[i]) > int(Array[i + 1]):
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")