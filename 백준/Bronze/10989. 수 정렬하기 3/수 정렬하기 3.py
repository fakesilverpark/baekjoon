import sys
input = sys.stdin.readline

n = int(input().strip())
num = [0] * 10001

for _ in range(n):
    m = int(input().strip())
    num[m] += 1

for i in range(1, 10001):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)
