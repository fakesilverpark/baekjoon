n = int(input())

menu = []

for _ in range(n):
    menu.append(int(input()))

price = 0
    
people = int(input())
for _ in range(people):
    price += menu[int(input()) - 1]
    
print(price)