limit = 100

firstNum = 0
secondNum = 1
sum = 0
for i in range(limit):
    firstNum = secondNum
    secondNum = sum
    sum = firstNum+secondNum
    if limit<sum:
        break
    print(sum)


    