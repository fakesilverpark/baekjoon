# TroyMartian, 적어도 3개의 안테나, 최대 4개의 눈
# VladSaturnian, 최대 6개의 안테나, 적어도 2개의 눈
# GraemeMercurian, 최대 2개의 안테나, 최대 3개의 눈

a = int(input())
e = int(input())

if (a >= 3 and e <= 4):
    print("TroyMartian")
if (a <= 6 and e >= 2):
    print("VladSaturnian")
if (a <= 2 and e <= 3):
    print("GraemeMercurian")