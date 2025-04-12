# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의 너비를 차지해야한다. 0은 4cm의 너비를 차지해야한다. 나머지 숫자는 모두 3cm의 너비를 차지한다.
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.

def f(n):
    if (n == 0):
        return 4
    elif (n == 1):
        return 2
    else:
        return 3

while (1):
    num = int(input())
    if (num == 0):
        break
    else:
        leng = 0
        cnt = 0
        while (num != 0):
            leng += f(num % 10)
            cnt += 1
            num //= 10
        print(leng + 1 * (cnt + 1))