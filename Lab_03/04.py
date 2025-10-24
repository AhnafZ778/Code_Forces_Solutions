import sys

input = sys.stdin.readline

def matrix_multiplication(result, array, mod = 1000000007):
    answer = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                answer[i][j] += result[i][k] * array[k][j]
                answer[i][j] %=mod
    return answer 
 
 
def matrix_exponentiation(array, exponent, mod = 1000000007):
    result = [[1,0],[0,1]]
    x = exponent
    while x > 0:
        if x % 2 == 1:
            result = matrix_multiplication(result, array)
        array = matrix_multiplication(array, array)
        x //= 2
    return result

test_cases = int(input())
for _ in range(test_cases):
    
    matrix = list(map(int, input().split()))
    exponent = int(input())
    first = matrix[:2]
    second = matrix[2:]
    two_d = [[0,0], [0,0]]
    for i in range(len(two_d)):
        two_d[0][i] = first[i]
    
    for i in range(len(two_d)):
        two_d[1][i] = second[i]
    
    result = matrix_exponentiation(two_d, exponent)
    for i in range(len(result)):
        for j in range(len(result)):
            print(int(result[i][j]), end = " ")
        print()
    
    