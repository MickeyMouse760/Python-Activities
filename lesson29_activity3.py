class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self, x, y):
        print("({x}, {y})".format(2, 3))
ob = point(2, 3)
print(ob.x,",", ob.y)