import sys

def fast_power_mod(a, b, mod = 107):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a**2) % mod
        b //= 2
    return result


input = sys.stdin.readline

a, b = map(int, input().split())

print(fast_power_mod(a, b))