def onnoff(i):
    if (i==0):
        return 1
    else:
        return 0
def bns(n, m):
    if (n>m):
        return m
    else:
        return n

n = int (input())

switch = []
while(1):
    if (len(switch)==n):
        break
    else:
        switch+=list( map (int, input().split()) )

popul = int (input())

student = []

for _ in range(popul):
    student.append( list ( map (int, input().split()) ) )

for i in student:
    c=i[1]
    if (i[0]==1):
        for j in range(1,n//c+1):
            switch[j*c-1] = onnoff(switch[j*c-1])
    else:
        switch[c-1] = onnoff(switch[c-1])
        small = bns(c-1, n-c)
        for l in range (small+1):
            if (switch[c-1-l]==switch[c-1+l]):
                switch[c-1-l]=onnoff(switch[c-1-l])
                switch[c-1+l]=onnoff(switch[c-1+l])
            else:
                break
cnt=0
for i in switch:
    cnt+=1
    if (cnt==20):
        print(i)
        cnt=0
    else:
        print(i,end=" ")
