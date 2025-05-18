class myclass:
    __privateVar = ("This is private")
    print(__privateVar)
ob = myclass()
print("This is private",ob.__privateVar)