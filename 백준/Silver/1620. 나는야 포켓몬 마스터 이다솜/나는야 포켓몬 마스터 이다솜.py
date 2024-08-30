n, m = map(int, input().split())

dictInformation = {}

for i in range(n):
    name = input()
    dictInformation[name] = str(i+1)
    dictInformation[str(i+1)] = name

for i in range(m):
    print(dictInformation[input()])