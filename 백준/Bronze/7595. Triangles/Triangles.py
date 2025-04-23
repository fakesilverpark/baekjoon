while (1):
    num = int(input())
    if (num == 0):
        break
    else:
        for i in range(num):
            print("*" * (i + 1))