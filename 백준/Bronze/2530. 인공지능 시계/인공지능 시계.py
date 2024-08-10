a,b,c=map(int,input().split())
n=int(input())

time=a*3600+b*60+c+n

t=time//3600
print(t-24*(t//24),end=" ")
time%=3600
print(time//60,end=" ")
print(time%60)