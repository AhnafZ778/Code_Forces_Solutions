import sys

input = sys.stdin.readline

total_students = int(input())
IDs = input()
ID = IDs.split()
Marks = input()
Mark = Marks.split()

swaps = 0
for i in range(total_students - 1):
    index = i
    maximum = int(Mark[i])
    for j in range(i+1 , total_students):
        if int(Mark[j]) > maximum:
            maximum = max(maximum, int(Mark[j]))
            index = j
        elif int(Mark[j]) == maximum:
            if int(ID[j]) < int(ID[index]):
                index = j
    if index != i:
        if int(Mark[i]) <= int(Mark[index]):
            Mark[i], Mark[index] = Mark[index], Mark[i]
            ID[i], ID[index] = ID[index], ID[i]
            swaps += 1

print("Minimum swaps:", swaps)
for i in range(len(Mark)):
    print(f"ID: {int(ID[i])} Mark: {int(Mark[i])}")
        
    
