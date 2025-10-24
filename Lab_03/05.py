import sys 

input = sys.stdin.readline

test_cases = int(input())

def fast_power_mod(a, b, mod = 107):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a**2) % mod
        b //= 2
    return result


def fast_series(a, n, m):
    if n == 0:
        return 0
    if n == 1:
        return a % m
    if n % 2 == 0:
        series_half = fast_series(a, n // 2, m)
        power_half = fast_power_mod(a, n // 2, m)
        return (series_half + power_half * series_half) % m
    else:
        return (fast_series(a, n - 1, m) + fast_power_mod(a, n, m)) % m

for i in range(test_cases):
    a, n, m = map(int, input().split())
    
    print(fast_series(a, n, m))
    
    
    
