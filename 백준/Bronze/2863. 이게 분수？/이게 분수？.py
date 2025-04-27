a, b = map(int, input().split())
c, d = map(int, input().split())

l = [a/c + b/d, c/d + a/b, d/b + c/a, b/a + d/c]
m = max(l)

for i in range(len(l)):
    if l[i] == m:
        print(i)
        break