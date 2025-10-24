import sys

input = sys.stdin.readline

def non_divisible_locator(position, divisor):
    left, right = 1, position * divisor
    while left < right:
        mid = (left + right) // 2
        numbers_not_divisible = mid - (mid // divisor)
        if numbers_not_divisible < position:
            left = mid + 1
        else:
            right = mid
    return left

test_cases = int(input())
answers = []
for _ in range(test_cases):
    position, divisor = map(int, input().split())
    answers.append(non_divisible_locator(position, divisor))

for i in answers:
    print(i)