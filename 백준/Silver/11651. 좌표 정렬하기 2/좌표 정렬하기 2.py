n=int(input())
points=[]
for i in range(n):
    apoint=input().split()
    apoint[0]=int(apoint[0])
    apoint[1]=int(apoint[1])
    points.append(apoint)
points.sort(key=lambda x: (x[1], x[0]))
for i in points:
    print(i[0],i[1])