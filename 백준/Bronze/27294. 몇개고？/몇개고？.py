t, s = map(int, input().split())

time = ""

if (t <= 11):
    time = "아침"
elif (t <= 16):
    time = "점심"
else:
    time = "저녁"

if (s == 1 or time != "점심"):
    print(280)
elif (time == "점심" and s == 0):
    print(320)