n = int(input())

m=50000

for i in range(n//3+1):
    for j in range(n//5+1):
        t=i*3+j*5
        if (i*3+j*5==n):
            if (m>t):
                m=t
                cnt=i+j
if (m==50000):
    cnt=-1
print(cnt)