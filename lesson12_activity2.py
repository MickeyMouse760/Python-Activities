num = int(input("Enter a number "))
number = 0
for i in range(num):
    for j in range(1, i + 1):
        print(number, end="")
        number = number + 1
    print("")
