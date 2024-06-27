N=int(input(""))
n=[]
for i in range(N):
    num=int(input(""))
    n.append(num)
n.sort()
for i in range(N):
    print(n[i])