n = int(input())

meme_list = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]

ox = 0

for _ in range(n):
    if (input() not in meme_list):
        ox += 1
if (ox != 0):
    print("Yes")
else:
    print("No")