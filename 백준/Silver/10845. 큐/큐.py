from sys import stdin
input = stdin.readline
n=int(input())
queue=[]
for _ in range(n):
    command=input().split()
    if (len(command)==2):
        queue.append(command[1])
    elif (command[0]=='pop'):
        if (len(queue)!=0):
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif (command[0]=='size'):
        print(len(queue))
    elif (command[0]=='empty'):
        if (len(queue)!=0):
            print(0)
        else:
            print(1)
    elif (command[0]=='front'):
        if (len(queue)!=0):
            print(queue[0])
        else:
            print(-1)
    elif (command[0]=='back'):
        if (len(queue)!=0):
            print(queue[-1])
        else:
            print(-1)