a,b,c=map(int,input().split())
n=int(input())
time=a*3600+b*60+c+n
print(time//3600-24*((time//3600)//24),end=" ")
time%=3600
print(time//60,end=" ")
time%=60
print(time)