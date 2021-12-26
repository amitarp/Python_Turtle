import turtle

turtle.width(2)
turtle.speed(10)

#loop for pattern
for i in range(10):
    turtle.circle(100)
    turtle.right(36)

turtle.screensize(canvwidth=400,canvheight=300,bg='blue')

turtle.done()