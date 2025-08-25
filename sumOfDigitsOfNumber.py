import math
number = 8938980

sum =0

for i in range(int(math.log10(number))+1):
    
    sum = sum + number%10  
    number = int(number/10)  

print(sum)