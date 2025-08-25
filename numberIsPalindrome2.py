number = 10012
originalNum=number
reversed = 0
while number>0:
    # print(number/10)
    lastNum = number%10
    number = int(number/10)
    reversed = reversed *10 +lastNum
print(reversed)

if originalNum==reversed:
    print("number is Palindrome")
else:
    print("Not a Palindrome")