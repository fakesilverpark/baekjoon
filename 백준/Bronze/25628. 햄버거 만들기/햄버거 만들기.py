a, b = map(int, input().split())

if a < 2 or b < 1:
    print(0)
else:
    print(min(a // 2, b))