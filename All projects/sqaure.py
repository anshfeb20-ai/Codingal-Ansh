import turtle
turtle.Screen().bgcolor('white')
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
polygon.color('black')

side = 100
angle = 90
i=0

for i in range(4):
    polygon.forward(side)
    polygon.right(90)
turtle.done()

