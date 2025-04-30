s1={1,2,3}
s2={'a','b','c'}
resu=list(zip(s1,s2))
print(resu)
l1=[1,2,3,4]
l2=[10,20,30,40]
print()
for x, y in zip(l1, l2[::-1]):
    print(x, y)
stock=['reliance','infosys','tcs']
prices=[2175,1127,2750]
dic={stock: prices for stock,
     prices in zip(stock, prices)}
print('\n{}'.format(dic))