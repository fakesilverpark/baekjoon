n = int(input())

l = []

for _ in range(n):
    n, m = map(int, input().split())
    if m - n >= 0:
        l.append(m)
        continue
        
if l == []:
    print(-1)
else:
    print(min(l))