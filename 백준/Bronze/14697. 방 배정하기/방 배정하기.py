a,b,c,r=map(int,input().split())
cnt=0
if (r%a==0):
    print(1)
elif (r%b==0):
    print(1)
elif (r%c==0):
    print(1)
else:
    for ai in range (r//a+1):
        if (cnt!=0):
            break
        aroom=r
        aroom-=ai*a
        for bi in range(aroom//b+1):
            if (cnt!=0):
                break
            broom=aroom
            broom-=bi*b
            for ci in range(broom//c+1):
                croom=broom
                croom-=ci*c
                if (croom==0):
                    cnt+=1
                    break
    if (cnt==0):
        print(0)
    else:
        print(1)