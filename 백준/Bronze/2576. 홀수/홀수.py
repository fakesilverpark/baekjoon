result = 0
minimum = 101
for _ in range(7):
    n = int(input())
    if (1&n):
        result += n
        if (n < minimum):
            minimum = n

if (minimum == 101):
    print(-1)
else:
    print(result)
    print(minimum)