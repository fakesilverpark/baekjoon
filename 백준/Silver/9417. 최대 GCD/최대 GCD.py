def gcd(a,b): #a-숫자1 b-숫자2 c-나눈 나머지
    if (b!=0):
        return gcd(b,a%b)
    else:
        return a

n=int(input())
for i in range(n):
    gcd_max=0
    numbers=input().split()
    leng=len(numbers)
    for j in range(leng):
        for l in range(1,leng):
            if (j==l):
                break
            else:
                if (int(numbers[j])==int(numbers[l])):
                    t=int(numbers[j])
                else:
                    t=gcd(int(numbers[j]),int(numbers[l]))
                if (t>gcd_max):
                    gcd_max=t
    print(gcd_max)