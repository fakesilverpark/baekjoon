def r(n, s, f, idx, l):
    if (idx==l):
        if (s==f):
            print("yes")
            return
        else:
            print("no")
            return
    else:
        s=s+n[l-idx-1:]
        n=n[:l-idx-1]
        r(n,s,f,idx+1,l)
n=1
while (1):
    n=input()
    if (int(n)==0):
        break
    else:
        if (len(n)==1):
            print("yes")
            continue
        else:
            l=len(n)//2
            if (len(n)%2==1):
                f=n[:l]
                b=n[l+1:]
            else:
                f=n[:l]
                b=n[l:]
            s=r(b,"",f,0,l)