punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
string ="Hello WorlD! how's is*&^^*&^*&%^$^^%&%& going dude"
new=""
for char in string:
    is_punc=False
    for p in punctuation:
        if char == p:
            is_punc=True
    if is_punc:
        new = new+""
    else :
        new = new+char

print(new)
