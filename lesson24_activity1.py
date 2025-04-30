num1=[1,4,7,9]
num2=[2,4,9,12]
res=map(lambda x,y: x+y, num1, num2)
print("Addition of 2 lists:")
print(res)
numbers=[2,5,8,17,31]
def square(n):
    return n*n
squared=list(map(square, numbers))
print("\nSquared numbers in a list:")
print(squared)