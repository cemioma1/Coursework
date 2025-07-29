import math
x1, y1= eval(input('Enter a point for first triangle: (x1, y1):'))
x2, y2 = eval(input('Enter a point for second triangle: (x2, y2):'))
x3, y3 = eval(input('Enter a point for third triangle: (x3, y3):'))
side1 = math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)
side2 = math.sqrt ((x1 - x3)**2 + (y1 - y3)**2)
side3 = math.sqrt ((x3 - x2)**2 + (y3 - y2)**2)
s = (side1 + side2 + side3) / 2

area = math.sqrt (s * (s - side1) * (s - side2) * (s - side3))
print (f"The area of the triangle is: {area:.2f}")