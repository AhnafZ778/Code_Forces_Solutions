import sys

input = sys.stdin.readline

test_cases = int(input())
answers = []
for i in range(test_cases):
    position, divisor = map(int, input().split())
    current = 0
    count = 1
    x = position + (position // divisor)
    answers.append(x)

for i in answers:
    print(i)
        