import sys
import math
input = sys.stdin.readline

array_size = int(input())

array = list(map(int, input().split()))

def arranger(array):
    if len(array) < 1:
        return
    mid = math.ceil(len(array)/2) - 1
    result = []
    root = array[mid]
    result.append(root)
    left = arranger(array[:mid])
    right = arranger(array[mid+1:])
    if left:
        result.append(left)
    if right:
        result.append(right)
    return result


answer = arranger(array)
answer = str(answer)
# print(answer)
i = 0
while i < len(answer):
    if "9" >= answer[i] >= "0":
        # print(answer[i])
        count = i
        s1 = ""
        while "9" >= answer[count] >= "0":
            s1 += answer[count]
            count += 1
        print(s1, end = " ")
        i = count
        continue
    i += 1
        
    