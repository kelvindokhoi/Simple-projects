numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def checkFirst(number): #Chia lay du de co don vi
    a = number[0]%10
    for i in range(len(number)):
        if number[i]%10 != a:
            return False
    return True
def checkSecond(number): #Chia lay nguyen de co hang chuc
    a = number[0]//10
    for i in range(len(number)):
        if number[i]//10 != a:
            return False
    return True
def checkAll(numbers):
    print(f"The inputed array: {numbers}")
    print(checkFirst(numbers) or checkSecond(numbers))

checkAll(numbers_x)
checkAll(numbers_y)