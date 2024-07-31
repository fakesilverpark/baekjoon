from collections import deque

num=int(input()) #입력받을 개수
total_cnt=0
for i in range(num+1):
    number=deque(str(i))
    cnt=number.count('3')
    cnt+=number.count('6')
    cnt+=number.count('9')
    total_cnt+=cnt
print(total_cnt)