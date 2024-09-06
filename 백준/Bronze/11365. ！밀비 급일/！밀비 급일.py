while (1):
    n = input()
    if (n == 'END'):
        break
    else:
        n = list(n)
        n.reverse()
        for i in n:
            print(i, end="")
        print("")