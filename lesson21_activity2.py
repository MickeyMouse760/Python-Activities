def palindrome(a):
    e = len(a)-1
    s = 0
    while(s<e):
        if(a[s] != a[e]):
            return False
        else:
            s+=1
            e-=1
        return True
a = (1,2,4,4,2,1)
if palindrome(a) == True:
    print("the tuple is a palindrome")
else:
    print("the tuple is not a palindrome")