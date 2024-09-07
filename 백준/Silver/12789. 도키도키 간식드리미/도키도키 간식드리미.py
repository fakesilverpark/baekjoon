from collections import deque

n = int(input())

person = deque(map(int, input().split()))

temp = deque([])

for i in range(1, n+1):
    if i in person:
        idx = person.index(i)
        for j in range(idx):
            temp.appendleft(person[j])
        person = deque(list(person)[idx+1:])
    elif (temp[0] == i):
        temp.popleft()

    else:
        print("Sad")
        break
else:
    print("Nice")