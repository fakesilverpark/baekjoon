n=[1,2,3]
while (1):
    n=input().split(" ")
    n=list(map(int,n))
    n.sort()
    if (n[-1]+n[1]+n[0]==0):
        break
    else:
        if (n[-1]>=n[0]+n[1]):
            print("wrong")
            continue
        else:
            s=n[-1]**2
            l=n[0]**2+n[1]**2
            if (s==l):
                print("right")
                continue
            else:
                print("wrong")
                continue