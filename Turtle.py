import turtle

turtle.speed(30)

turtle.color('purple', 'light blue')
turtle.begin_fill()
for i in range(72):
    turtle.forward(300)
    turtle.left(175)
    
turtle.end_fill()

turtle.forward(130)
turtle.color('red')
turtle.begin_fill()
for i in range(72):
    turtle.forward(40)
    turtle.left(175)

turtle.end_fill()

input()