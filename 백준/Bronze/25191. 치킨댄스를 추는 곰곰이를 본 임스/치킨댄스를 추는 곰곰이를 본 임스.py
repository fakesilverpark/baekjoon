chicken = int(input())

coke, beer = map(int, input().split())
coke //= 2

if (coke + beer >= chicken):
    print(chicken)
else:
    print(coke + beer)