cups = [1, 0, 0]

for _ in range(int(input())):
    x, y = map(int, input().split())
    temp = cups[x - 1]
    cups[x - 1] = cups[y - 1]
    cups[y - 1] = temp

print(cups.index(1) + 1)