N=int(input(""))
n=[]
for i in range(N):
    num=int(input(""))
    n.append(num)
n.sort()
n.reverse()
for i in range(N):
    print(n[i])