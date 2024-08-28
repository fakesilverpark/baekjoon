from sys import stdin

input = stdin.readline

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

h = {}

for i in n:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1

for i in m:
    if i in h:
        print(h[i], end = " ")
    else:
        print(0, end = " ")