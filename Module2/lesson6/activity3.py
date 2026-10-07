import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
polygon.color("black")

num = 10
distance = 100

for i in range(num):
    polygon.forward(distance)
    polygon.right(90)
    distance = distance - 10
turtle.done()
    