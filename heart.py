import turtle


turtle.speed(5)
turtle.bgcolor('black')
turtle.pensize(10)

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('white','red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)
func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.hideturtle()

turtle.end_fill()

turtle.done()