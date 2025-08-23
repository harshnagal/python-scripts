string ="mostFreqCharachter"

mainCounter = 0
mostrepeatedChar=[]
for char in string:
    tempcounter = 0
    for secondchar in string:
        if char==secondchar:
            tempcounter+=1
    if tempcounter>mainCounter:
        mostrepeatedChar=char

print(mostrepeatedChar)

