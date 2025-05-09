class IOString():
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("Please enter the string: ")
    def printstring(self):
        print("The result is:",self.str1.upper())
ob = IOString()
ob.getstring()
ob.printstring()