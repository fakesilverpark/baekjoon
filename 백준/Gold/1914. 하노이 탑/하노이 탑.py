def hanoi_num(flo):
    if flo==1:
        return 1
    else:
        return 2**flo-1
def hanoi(n,s,e,t):
    if n==1:
        print(f'{s} {e}')
        a=1
        return 1
    else:
        hanoi(n-1,s,t,e)
        print(f'{s} {e}')
        hanoi(n-1,t,e,s)
        return 0
n=int(input())
print(hanoi_num(n))
if n<=20:
    hanoi(n,1,3,2)