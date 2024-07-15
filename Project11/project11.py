import os
os.system("clear")
os.system("cls")

Num = input("Input your desiring number:\t")

for i in range(len(Num)-1,-1,-1):
    print(Num[i],end=" ")