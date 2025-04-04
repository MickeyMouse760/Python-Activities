nums=[1, 3, 4, 73, 23, 42, 8]
print("original list:", nums)
for i in nums:
    nums+=i
print("adding the numbers together:", nums)
nums = nums/len(nums)
print("the average of the numbers:", nums)
print("smallest number:", min(nums))
print("largest number:", max(nums))