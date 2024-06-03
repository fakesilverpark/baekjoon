s=input()
word=[]
for i in range(0,len(s)):
    word.append(s[i])
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cnt=0
M=0
idx=0
d=1
for i in range(0,len(a)):
    cnt=s.count(a[i])+s.count(A[i])
    if (cnt>M):
        M=cnt
        idx=i
        d=0
    elif (cnt==M):
        d=2
    else:
        continue;
if (d==2):
    print("?")
else:
    print(A[idx])