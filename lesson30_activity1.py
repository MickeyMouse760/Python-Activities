from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value = ",x)
    @abstractmethod
    def task(self):
        print("We are inside of absclass fucntion")
class test_class(Absclass):
    def task(self):
        print("We are inside of the test class")
test_ob = test_class()
test_ob.task()
test_ob.print(100)