try:
    num1,num2=eval(input("Please enter 2 numbers separated by a comma: "))
    print("Number 1 divided by number 2 is:", num1/num2)
except ZeroDivisionError:
    print("The second number must be greater than 0")
except SyntaxError:
    print("Enter a comma to separate the numbers")
except ValueError:
    print("You must enter numbers")
else:
    print("There is no error")
finally:
    print("This code will run no matter what")