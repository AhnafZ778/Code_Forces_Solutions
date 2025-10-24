import sys
 
input = sys.stdin.readline
 
a = int(input())
 
for i in range(a):
    b = input()
    zzz, c,d,e = b.split()
    if d == "+":
        print(float(c) + float(e))
    elif d == "*":
        print(float(c) * float(e))
    elif d == "-":
        print(float(c) - float(e))
    elif d == "/":
        print(float(c) / float(e))
    