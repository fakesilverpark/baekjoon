s=input()
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cnt=0
for i in a:
    for j in range(0,len(s)):
        if (s[j]==i):
            print(j,end=" ")
            cnt+=1
            break;
    if (cnt==0):
        print(-1,end=" ")
    cnt=0
