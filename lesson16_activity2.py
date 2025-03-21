for num in range(25):
    if num%20==0:
        print("Twist")
    elif num%15==0:
        pass
    elif num%10==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
