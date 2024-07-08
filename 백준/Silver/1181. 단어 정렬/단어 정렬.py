n=int(input())
words=[]
idx=[]
w=input()
cnt=0
words.append(w)
for i in range(n-1):
    w=input()
    for j in range(len(words)):
        if (words[j] == w):
            cnt=0
            break
        else:
            cnt+=1
            continue
    if (cnt==len(words)):
        words.append(w)
    cnt=0
words.sort()
words.sort(key=len)
for i in range(len(words)):
    print(words[i])