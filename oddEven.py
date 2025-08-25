def numberIsEven(number):
    if number%2==0:
        return True
    else:
        return False

number=11
if numberIsEven(number):
    print("Number is Even")
else:
    print("Number is Odd")