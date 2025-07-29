import turtle
turtle.showturtle()
square_size = 50
for row in range (8):
    for col in range(8):
        x = col * square_size - 200
        y = 200 - row * square_size

    turtle.penup()
    turtle.goto(4,0)
    turtle.pendown()
    if (row + col) % 2 == 0:
        turtle.fillcolor("black")
        turtle.begin_fill()

        for _ in range (4):
            turtle.forward(20)
            turtle.right(90)
            if (row + col) % 2 == 0:
                    turtle.end_fill()
turtle.hideturtle()
turtle.done()
