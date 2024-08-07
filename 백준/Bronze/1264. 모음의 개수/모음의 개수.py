from collections import deque

m=['a','e','i','o','u','A','E','I','O','U']

while (1):
    s=input()
    if (s=='#'):
        break
    else:
        cnt=0
        s=list(deque(s))
        while (len(s)!=0):
            c=s[-1]
            del s[-1]
            if c in m:
                cnt+=1
        print(cnt)