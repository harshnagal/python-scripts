num = 4544654
original_num=num
reversed_num=0

while num>0:
    last_digit = num%10
    
    reversed_num = reversed_num * 10 + last_digit
    num = num/10
    num = int(num)

if reversed_num==original_num:
    print("number is palindrome")
else :
    print("not palindrom")