number = 8888387
import math

reversed = 0
for i in range (int(math.log10(number)+1)):
    # print(number)
    lastNum = number%10
    number = int(number/10)
    
    reversed = reversed*10 + lastNum
print(reversed)
