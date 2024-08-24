n = int (input())

def f(n, result):
    
    if (n == 1 or n == 0):
        print(result)
        return 0

    else:
        f(n-1, result * n)

f(n, 1)