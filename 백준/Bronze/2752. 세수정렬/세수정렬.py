a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
for i in a:
    print(i,end=" ")