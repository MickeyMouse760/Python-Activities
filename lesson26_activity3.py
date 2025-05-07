class turtle:
    species = 'reptile'
    def __init__(self, name, age):
        self.name=name
        self.age=age
ob = turtle("Jason", 57)
tl = turtle("Harry", 49)
print(ob.name,"is a",ob.species)
print(ob.name,"is",ob.age,"years old")
print(tl.name,"is also a",tl.species)
print(tl.name,"is",tl.age,"years old")