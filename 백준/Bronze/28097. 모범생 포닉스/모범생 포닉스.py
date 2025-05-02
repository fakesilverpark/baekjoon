n = int(input())
plan = list(map(int, input().split()))

time = 8 * (n - 1) + sum(plan)
print(time // 24, time % 24)