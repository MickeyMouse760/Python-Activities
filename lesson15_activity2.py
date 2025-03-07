def mul3(num):
    return num*num*num

def by3(num):
    if num%3==0:
        return(mul3(num))
    else:
        return False
print(by3(9))
print(by3(4))