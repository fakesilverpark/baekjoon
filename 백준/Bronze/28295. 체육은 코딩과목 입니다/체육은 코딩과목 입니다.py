state = 0

for _ in range(10):
    n = int(input())
    if n == 1:
        state += 90
    elif n == 2:
        state += 180
    elif n== 3:
        state += 270

state %= 360
        
if state == 0:
    print("N")
elif state == 90:
    print("E")
elif state == 180:
    print("S")
else:
    print("W")