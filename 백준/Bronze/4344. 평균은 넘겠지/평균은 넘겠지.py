import statistics

num=int(input())

for _ in range(num):
    
    result=0
    cnt=0
    
    number=input().split()
    num2=int(number[0])
    number=number[1:]
    
    for i in range(num2):
        number[i]=int(number[i])
    
    result=statistics.mean(number)
    
    for i in number:
        if (i>result):
            cnt+=1
    a=cnt/num2*100
    print("%.3f" %a,end="%\n")