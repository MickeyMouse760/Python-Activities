num = int(input("Please enter the number of rows "))
for i in range(num):
    for j in range(i + 1):
        print("*", end=(""))
    print("")