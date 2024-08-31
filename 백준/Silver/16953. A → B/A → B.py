a, b = map(int, input().split())

def computeUntilA(a, b, cnt):
    if (b < a):
        print(-1)
        return 0
    elif (a == b):
        print(cnt)
        return 0
    else:
        if (b % 2 == 0):
            return computeUntilA(a, b//2, cnt+1)
        elif (str(b)[-1] == '1'):
            b = str(b)
            return computeUntilA(a, int(b[:len(b)-1]), cnt+1)
        else:
            print(-1)
            return 0

computeUntilA(a, b, 1)