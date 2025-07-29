'''(Turtle: draw four squares) Write a program that draws four squares in the center
of the screen, as shown in Figure 1.18a'''

import _tkinter
import turtle
#square
turtle.showturtle()
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)
turtle.goto(-100,100)
#cross
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.goto(0,-100)
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.goto(100,0)
turtle.done()
