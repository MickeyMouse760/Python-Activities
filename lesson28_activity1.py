class vehicle():
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage
class bus(vehicle):
    pass
ob = bus("Volvo", "270")
print("The bus name is:",ob.name)
print("The bus mileage is:",ob.mileage)
