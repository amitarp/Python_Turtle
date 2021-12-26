import turtle

turtle.speed(30)
turtle.pensize(5)
turtle.bgcolor('black')

for i in range(6):
    for colors in ['red','magenta','green','cyan','white','blue','yellow']:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
turtle.done()