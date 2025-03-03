leng = int(input())

if (leng >= 620 and leng <= 780):
    print("Red")
elif (leng >= 590 and leng < 620):
    print("Orange")
elif (leng >= 570 and leng < 590):
    print("Yellow")
elif (leng >= 495 and leng < 570):
    print("Green")
elif (leng >= 450 and leng < 495):
    print("Blue")
elif (leng >= 425 and leng < 450):
    print("Indigo")
else:
    print("Violet")