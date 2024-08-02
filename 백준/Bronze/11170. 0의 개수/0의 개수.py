from collections import deque

num=int(input())

for _ in range(num):
    n, m=map(int,input().split())

    total_cnt=0

    for i in range(n,m+1):
        number=deque(str(i))
        cnt=number.count('0')
        total_cnt+=cnt
    print(total_cnt)