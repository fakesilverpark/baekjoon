while (1):
    i=input()
    if (i!="# 0 0"):
        i=i.split()
        print(i[0],end=" ")
        if (int(i[1]) > 17):
            print("Senior")
        elif (int(i[2]) >= 80):
            print("Senior")
        else:
            print("Junior")
    else:
        break