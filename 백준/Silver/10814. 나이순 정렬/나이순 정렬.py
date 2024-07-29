n=int(input())
information=[]
for i in range(n):
    ann=input().split()
    ann[0]=int(ann[0])
    information.append(ann)
information.sort(key=lambda x:x[0])
for i in information:
    print(i[0],i[1])