import sys

input = sys.stdin.readline

T = int(input())
N = input()
arr = N.split()
if T == 1:
    print(int(arr[0]))
else:
    check = False
    while not check:
        for i in range(len(arr)-1):
            if int(arr[i]) % 2 == 0 and int(arr[i + 1]) % 2 == 0:
                if int(arr[i]) > int(arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            elif int(arr[i]) % 2 != 0 and int(arr[i + 1]) % 2 != 0:
                if int(arr[i]) > int(arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        check = True
        for i in range(len(arr)-1):
            if int(arr[i]) % 2 == 0 and int(arr[i + 1]) % 2 == 0:
                if int(arr[i]) > int(arr[i + 1]):
                    check = False
            elif int(arr[i]) % 2 != 0 and int(arr[i + 1]) % 2 != 0:
                if int(arr[i]) > int(arr[i + 1]):
                    check = False
    for i in arr:
        print(int(i), end = " ")
            