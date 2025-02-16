string1 = input("Please enter a word ")
string2 = ("")
for i in string1:
    string2 = i+string2
print("The word before reversing: ", string1)
print("The word after reversing: ", string2)