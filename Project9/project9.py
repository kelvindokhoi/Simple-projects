import os
from math import ceil
os.system("clear")
os.system("cls")


Cnum = input("Enter the number for palindrome checking:\t")
lengthN = len(Cnum)

def midPoint_Num(a):
    return int(ceil(a/2))
mid_right_Num = midPoint_Num(lengthN)

def checkPalin(a,l, mid):
    if l//2==mid-1:
        print("Case 1") #Case le so
        waytogo = l-mid
        print(f"Waytogo: {waytogo}")
        for i in range(waytogo):
            print(f"step: {i}")
            print(f"right: {mid+i}")
            print(f"left: {mid-i-2}")
            if not a[mid-2-i]==a[mid+i]:
                return False
        return True
    else:
        print("Case 2") #Case chan so
        waytogo = l-mid
        print(f"Waytogo: {waytogo}")
        for i in range(waytogo):
            print(f"step: {i}")
            print(f"left: {mid-1-i}")
            print(f"right: {mid+i}")
            if not a[mid-1-i]==a[mid+i]:
                return False
        return True
    
answer = checkPalin(Cnum,lengthN, mid_right_Num)

if answer:
    print("This is a palindrome.")
else:
    print("Not a palindrome.")
