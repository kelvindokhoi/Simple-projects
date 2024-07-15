arrayNums = []
counter = 0
while counter > -1:
    arrayNums.append(input("Input a number to put into array, enter to stop: "))
    if arrayNums[counter] == "":
        break
    counter += 1
results = []
for i in range(len(arrayNums)-1):
    if int(arrayNums[i]) % 5 == 0:
        results.append(arrayNums[i])
print(results)