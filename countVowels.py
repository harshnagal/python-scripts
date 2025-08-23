vowels = "aeiouAEEIOU"
string="Stargazing"
counter=0
for i in range(len(string)):
    for j in range(len(vowels)):
        if string[i]==vowels[j]:
            counter+=1
print(counter)