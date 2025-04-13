def y(numbers):
    result = []
    for i in numbers:
        result.append(((i // 30) + 1) * 10)
    return result

def m(numbers):
    result = []
    for i in numbers:
        result.append(((i // 60) + 1) * 15)
    return result

N = int(input())
n = list(map(int, input().split()))

Y = sum(y(n))
M = sum(m(n))

if (Y == M):
    print(f'Y M {Y}')
elif (Y > M):
    print(f'M {M}')
else:
    print(f'Y {Y}')