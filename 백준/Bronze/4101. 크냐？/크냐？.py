#조건문에서 break를 만나기전까지 무한반복 한다.
while (1):
		
		#a, b 값을 입력받는다
    a,b=map(int,input().split())

		#a, b 값이 모두 0이면 while문을 탈출한다.
    if (a==0 & b==0):
        break
		
		#아니라면 a, b의 대소관계를 비교해서 출력한다.
    else:
        if (a>b):
            print("Yes")
        else:
            print("No")