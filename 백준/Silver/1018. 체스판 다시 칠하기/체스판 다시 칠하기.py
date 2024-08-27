from collections import deque

def checkcheck_b(arr):
    cnt = 0
    check = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    for i in range(64):
        if (check[i] != arr[i]):
            cnt += 1
    return cnt

def checkcheck_w(arr):
    cnt = 0
    check = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    for i in range(64):
        if (check[i] != arr[i]):
            cnt += 1
    return cnt

def checking(arr):
    b = checkcheck_b(arr)
    w = checkcheck_w(arr)
    if (b >= w):
        return w
    else:
        return b

n, m = map (int, input().split()) #n = 세로, m = 가로

chess = []

for _ in range(n):
    chess.append(input())

min_num = 64

for i in range(0, n-7):
    c = chess[i:i+8]
    for j in range(0, m-7):
        cstr = ""
        for l in c:
            cstr += str(l[j:j+8])
        cnt = checking(list(deque(cstr)))
        if (cnt < min_num):
            min_num = cnt
print(min_num)