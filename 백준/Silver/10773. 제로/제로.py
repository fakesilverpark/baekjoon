from collections import deque
n=int(input())
numbers = deque('')
cnt=0
new=0
summ=0
for i in range(n+1):
    if (i==n):
        for _ in range(cnt):
            numbers.pop()
    else:
        new=int(input())
        if (new!=0):
            for _ in range(cnt):
                numbers.pop()
            numbers.append(new)
            cnt=0
        else:
            cnt+=1
for i in numbers:
    summ+=i
print(summ)