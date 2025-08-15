s = input("Enter a string: ")
string = ""

for char in s:
    if char != " ":
        string += char

print("String without spaces:", string)
