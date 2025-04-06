def f(n):
    if (n == 0): return "0"
    elif (n > 0): return "+"
    else: return "-"

for _ in range(3):
    n = int(input())
    t = 0
    for _ in range(n):
        t += int(input())
    print(f(t))