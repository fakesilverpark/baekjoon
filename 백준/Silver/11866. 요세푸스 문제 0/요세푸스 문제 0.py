n, k = map (int, input().split())
num=[]
idx=0
for i in range(n):
    num.append(i+1)
print("<",end="")
l=len(num)
for i in range(n-1):
    idx+=k-1
    if (idx>=len(num)):
        l=len(num)
        idx-=l*(idx//l)
    print(num[idx],end=", ")
    num.pop(idx)
print(str(num[0])+">")