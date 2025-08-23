string = "7454547"

lenght = len(string)

reversed =""
for i in range(lenght):
    reversed = reversed + string[lenght-i-1]

if string==reversed:
    print("palindrome")
else :
    print("not palindrome")