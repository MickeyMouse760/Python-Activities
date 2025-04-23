dic = {'condingal':2,'is':2,'the':2,'best':2,'for':2,'coding':1}
print("The dictionary: ",dic)
k = 2
res = 0
for key in dic:
    if dic[key]==k:
        res+=1
print("\nFrequency of 2 is: "+str(res))