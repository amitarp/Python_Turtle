import turtle

turtle.speed(50)
def fleur():
    for i in range(150):
        turtle.circle(180-i,90)
        turtle.left(75)
        turtle.circle(180-i,90)
        turtle.left(20)

fleur()
turtle.hideturtle()
turtle.done()