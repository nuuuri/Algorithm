A = [[1, 2], [3, 4]]

def multi(arr1, arr2):
    return [[sum(i*j%1000 for i, j in zip(row, col)) for col in zip(*arr2)] for row in arr1]

# 1. 재귀 사용
def exp1(arr, n):
    if n == 1:
        return A

    if n%2:
        return multi(multi(exp1(arr, n//2), exp1(arr, n//2)), A)
    else:
        return multi(exp1(arr, n//2), exp1(arr, n//2))

# 2. 재귀 사용 X
def exp2(arr, n):
    result = [[1 if i==j else 0 for j in range(2)] for i in range(2)]

    while n:
        if n%2:
            result = multi(result, arr)

        arr = multi(arr, arr)
        n //= 2

    return result