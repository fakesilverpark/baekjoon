a, b = map(int, input().split())

def computeUntilA(b, cnt):
    if (b < a):
        print(-1)
        return 0
    elif (a == b):
        print(cnt)
        return 0
    else:
        if (b % 2 == 0):
            return computeUntilA(b//2, cnt+1)
        elif (str(b)[-1] == '1'):
            return computeUntilA(b//10, cnt+1)
        else:
            print(-1)
            return 0

computeUntilA(b, 1)