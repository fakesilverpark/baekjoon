from collections import deque
num=int(input())
for i in range(num):
    deque_bracket=deque(input())
    cnt=0
    l=len(deque_bracket)
    for j in range(0,l):
        e=deque_bracket.popleft()
        if (e=="("):
            cnt+=1
            if (j==l-1):
                cnt=5
                break
        else:
            cnt-=1
            if (j==0):
                break
        if (cnt<0):
            break
    if (cnt!=0):
        print("NO")
    else:
        print("YES")