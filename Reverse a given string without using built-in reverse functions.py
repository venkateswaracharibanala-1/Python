string = input("")
i=len(string)-1
rev=""
while i >= 0:
    rev += string[i]
    i -= 1
print(rev)
