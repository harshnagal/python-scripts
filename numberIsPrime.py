number = 37
import math

isPrime = True

for i in range(2,int(math.sqrt(number))+1):
    if number%i==0:
        isPrime=False

if (isPrime):
    print("Number is Prime")
else:
    print("Number is not a Prime Number")
        
    
