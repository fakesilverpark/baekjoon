#------설명---------

#어떤식으로 정렬해야할까?

#그냥 정렬하고 정렬된 것을 출력하는 문제 였다면 키나 몸무게 순으로 먼저 정렬하고 나머지를 하면 되겠지만 
#이건 덩치 등수를 구해서 각 덩치 등수를 입력 받은 순서대로 출력해야하기 때문에 그냥 정렬할 수는 없다. 
#그렇다면 어떻게 해야할까!!!
#→ 다시 생각해보니 굳이 정렬을 할 필요가 없다! 더한다!! 더하면 된다! 
#그 자리의 값과 다른 자리의 값을 비교해서 그 자리보다 큰 수의 개수만큼 더한다!!! 아하

#➔ 나 보다 큰 값의 개수 +1 = 나의 등수


#-------코드-------

num = int(input()) #몇번 입력받을지를 정하는 변수
value_list=[] #입력받는 값을 저장할 빈 리스트

#x, y를 각각 입력받아 pers라는 리스트에 넣고 
#그 리스트를 다시 value_list에 넣어서 이차원 배열을 만든다
for i in range(num):
    pers=[]
    x, y=map(int,input().split(" "))
    pers.append(x)
    pers.append(y)
    value_list.append(pers)
    
#자신보다 큰 값의 개수 +1이 본인의 등수이므로 나머지 값이 본인보다 클때마다 score에 +1을 해준다.
for i in range(num):
    score=1
    for j in range(num):
        if (i!=j): #본인과 본인은 비교할 필요가 없다
		        #본인보다 키도 크고 몸무게도 많이 나가면 등수를 내린다.
            if ((value_list[i][0]<value_list[j][0]) & (value_list[i][1]<value_list[j][1])):
                score+=1
    print(score,end=" ") #공백 한칸으로 띄워서 한줄에 출력한다.