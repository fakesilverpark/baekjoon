n = int(input())
num = list(map(int, input().split()))

if (n == 1):
    print(num[0] ** 2)
elif (n == 2):
    print(num[0] * num[1])
else:
    num.sort()
    print(num[0] * num[-1])