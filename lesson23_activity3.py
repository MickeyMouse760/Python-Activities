import array as arr
array1 = arr.array('i',[3,4,6,8,3,5,7,3])
print('The original array:')
print(str(array1))
print("The number of occurances of 3:")
str(array1.count(3))
print(array1)
print("The array after reversing:")
array1.reverse()
print(str(array1))