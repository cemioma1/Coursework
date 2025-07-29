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