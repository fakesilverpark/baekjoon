N = int(input())
n = list(map(int, input().split()))

Y = 0
M = 0

def f():
    global Y, M
    for i in n:
        Y += (((i // 30) + 1) * 10)
        M += (((i // 60) + 1) * 15)

f()
        
if (Y == M):
    print(f'Y M {Y}')
elif (Y > M):
    print(f'M {M}')
else:
    print(f'Y {Y}')