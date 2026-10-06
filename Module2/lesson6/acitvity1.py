import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
num=6
side_length=70
angle=360/num
for i in range(num):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()