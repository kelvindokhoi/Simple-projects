import os

os.system("clear")
os.system("cls")

numTimes = input("Give me how many times do you want to repeat:\t")
k=0

def is_number(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

numberState = is_number(numTimes)
if numberState:
    numTimes = k = int(numTimes)
else:
    k = ord(numTimes)

def newPrint(a,k,stateN):
    if stateN:
       for i in range(a):
          print(a,end=" ")
    else:
        for i in range(k):
            print(a,end=" ")

def pSuper(a,k,stateN):
    if stateN:
       for i in range(1,a+1):
            newPrint(a,i,stateN)
            print("\n")
    else:
        for i in range(1,k+1):
            newPrint(a,i,stateN)
            print("\n")

pSuper(numTimes,k,numberState)