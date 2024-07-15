import os
os.system("clear")
os.system("cls")

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def checkOdd(a):
    if a%2==1:
        return True
    else:
        return False

def checkEven(a):
    if a%2==0:
        return True
    else:
        return False
    
result = []

for i in range(len(list1)):
    if checkOdd(list1[i]):
        result.append(list1[i])
    if checkEven(list2[i]):
        result.append(list2[i])

print(f"The result list is: {result}")