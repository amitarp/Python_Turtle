import turtle

turtle.speed(50)
def fleur():
    for i in range(150):
        turtle.circle(190-i,90)
        turtle.left(90)
        turtle.circle(190-i,90)
        turtle.left(18)

fleur()
turtle.hideturtle()
turtle.done()