value=[]
for i in range(3):
    value.append(input())
def check_type(value):
    if (value=='Fizz'):
        return 0
    elif (value=='Buzz'):
        return 0
    elif (value=='FizzBuzz'):
        return 0
    else:
        return 1
idx=0
for i in value:
    if (check_type(i)):
        break
    else:
        idx+=1
num=    (3-(idx))+int(value[idx])
if (num%15==0):
    print("FizzBuzz")
elif (num%3==0):
    print("Fizz")
elif (num%5==0):
    print("Buzz")
else:
    print(num)