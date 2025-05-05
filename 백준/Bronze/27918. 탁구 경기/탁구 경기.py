n = int(input())

d = 0
p = 0

for _ in range(n):
    temp = input()
    if temp == "D":
        d += 1
        if d - p >= 2:
            break
    else:
        p += 1
        if p - d >= 2:
            break

print(f'{d}:{p}')