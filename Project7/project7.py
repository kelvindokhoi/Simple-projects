import os
str_x = "Emma is good developer. Emma is a writer" #Given string
keyword = "Emma" # Given key

appearingTimes = 0

def normalCheck(a,b,startP):
    if len(b)>len(a):
        return False
    else:
        for i in range(len(b)-1):
            if not a[startP] == b[i]:
                return False
            else:
                startP+=1
        return True


for counterStr in range(len(str_x)):
    if str_x[counterStr]==keyword[0] and counterStr+len(keyword)<=len(str_x):
        if normalCheck(str_x,keyword,counterStr)==True:
            appearingTimes+=1

os.system('clear')
os.system('cls')
print(f"Appearing times: {appearingTimes}")