def f(n):
    global num
    if (num >= n):
        return n
    else:
        return num

num = int(input())

a, b, c = map(int, input().split())

print(f(a) + f(b) + f(c))