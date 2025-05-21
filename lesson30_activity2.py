class animal():
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and talk")
class snake(animal):
    def move(self):
        print("I can slither")
class dog(animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
h = human()
h.move()
s = snake()
s.move()
d = dog()
d.move()
l = lion()
l.move()