n, x = map(int,input().split())
l = list(map(int,input().split()))

m = (l[0] + l[1]) * x
for i in range(1, n - 1):
    temp = (l[i] + l[i + 1]) * x
    m = min([m, temp])
print(m)