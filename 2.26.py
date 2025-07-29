import turtle
import math
#prompt user for center and radius
radius = float(input("Enter the radius:"))
x = float(input("Enter the x-coordinate of center dot:"))
y = float(input("Enter the y-coordinate of the center dot:"))
#calculate area
area = math.pi * radius ** 2
#turtle
turtle.circle(radius)
turtle.penup()
turtle.goto(x,y)
turtle.write(f"{area:.2f}")

turtle.done()