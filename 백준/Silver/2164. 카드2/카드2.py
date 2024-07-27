num=int(input())
i=0
if (num==1):
    print(1)
else:
    for i in range(20):
        m=int(2**(i-1))
        n=int(2**i)
        if (num>m and num<=n):
            break
    print(2**i-(2**i-num)*2)