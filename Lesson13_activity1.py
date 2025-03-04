import turtle
turtle.Screen().bgcolor("aquamarine")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
length = 75
sides = 6
angle = 60
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()