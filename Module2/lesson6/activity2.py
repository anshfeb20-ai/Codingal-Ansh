import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()

polygon.fillcolor("blue")
polygon.begin_fill()
polygon.right(0)
polygon.forward(100)
polygon.left(120)
polygon.forward(100)
polygon.left(120)
polygon.forward(100)
polygon.end_fill()


polygon.penup()

polygon.goto(100,60)
polygon.setheading(240)
polygon.pendown()
polygon.begin_fill()
polygon.forward(100)
polygon.right(120)
polygon.forward(100)
polygon.right(120)
polygon.forward(100)
polygon.end_fill()

turtle.done()


# turtle.Screen().bgcolor("Aqua")
# board = turtle.Turtle()
 
# # first triangle for star
# board.forward(100) # draw base
 
# board.left(120)
# board.forward(100)
 
# board.left(120)
# board.forward(100)
 
# board.penup()
# board.right(150)
# board.forward(50)
 
# # second triangle for star
# board.pendown()
# board.right(90)
# board.forward(100)
 
# board.right(120)
# board.forward(100)
 
# board.right(120)
# board.forward(100)
 
# turtle.done()