def f(n):
    if (n == 0):
        return 4
    elif (n == 1):
        return 2
    else:
        return 3

while (1):
    num = int(input())
    if (num == 0):
        break
    else:
        leng = 0
        while (num != 0):
            leng += f(num % 10) + 1
            num //= 10
        print(leng + 1)