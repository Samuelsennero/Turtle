import turtle

turtle.speed(15)


#red house
turtle.color('red')
turtle.begin_fill()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

#door
turtle.left(180)
turtle.forward(150)
turtle.left(90)
turtle.forward(200)
turtle.color('black')
turtle.begin_fill()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

#window
turtle.color('red')
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.color('grey')
turtle.begin_fill()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

#roof


turtle.penup()
turtle.setposition(0, 150)
turtle.pendown()

turtle.color('black')
turtle.begin_fill()

turtle.right(150)
turtle.forward(174)
turtle.right(60)
turtle.forward(174)
turtle.right(150)
turtle.forward(300)
turtle.end_fill()

input()