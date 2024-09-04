import sys

def input():
    return sys.stdin.readline()

n = int(input())
num = [0] * 10001

for _ in range(n):
    m = int(input())
    num[m] += 1

for i in range(1, 10001):
    if (num[i] != 0):
        for _ in range(num[i]):
            print(i)