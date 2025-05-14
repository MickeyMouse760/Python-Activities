class employee():
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name,self.id_number)
class person(employee):
    def __init__(self, name, id_number, salary, boss):
        self.salary = salary
        self.boss = boss
        employee.__init__(self, name, id_number)
ob = person("Jacob", "195703", "$12500", "Mr. Watson")
ob.display()