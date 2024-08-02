from collections import deque

for _ in range(int(input())):

    total_cnt=0
    
    n, m=map(int,input().split())

    for i in range(n,m+1):
        total_cnt+=deque(str(i)).count('0')

    print(total_cnt)