n,m=map(int,input().split())

nSet=set()
for _ in range(n):
    nSet.add(input())

mSet=set()
for _ in range(m):
    mSet.add(input())

resultSet=list(nSet.intersection(mSet))
resultSet.sort()

print(len(resultSet))

for i in resultSet:
    print(i)