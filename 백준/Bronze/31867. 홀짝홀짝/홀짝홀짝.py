n = int(input())
num = [i % 2 for i in list(map(int, list(input())))]

odd = num.count(1)
even = num.count(0)

if even == odd:
    print(-1)
elif even > odd:
    print(0)
else:
    print(1)