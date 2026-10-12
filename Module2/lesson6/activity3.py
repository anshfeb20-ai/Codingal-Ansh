import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
polygon.color("black")

angle=90
distance = 100

for i in range(4):
    polygon.forward(distance)
    polygon.right(angle)
turtle.done()
    