word = input("Please enter a word.")
char = input("Please enter a character.")
i = 0
count = 0
while (i <= len(word)):
    if (word[i] == char):
        count = count + 1
    i = i + 1
print("The number of times ", char,"has occured in ", word,"is ", count)