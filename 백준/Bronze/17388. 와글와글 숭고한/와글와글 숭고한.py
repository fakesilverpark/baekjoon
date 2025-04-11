univ = {0: "Soongsil", 1: "Korea", 2: "Hanyang"}

x = list(map(int, input().split()))

if (sum(x) >= 100):
    print("OK")
else:
    m = min(x)
    for i in range(len(x)):
        if x[i] == m:
            print(univ[i])