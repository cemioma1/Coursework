
weight = int(input("Enter weight in pounds:"))
height = int(input("Enter feet:"))
inches = int(input ("Enter inches:"))
kg = weight / 2.205
total_inches = (height * 12) + inches
meters = total_inches * 0.0254
bmi = kg / (meters ** 2)
print (f"BMI is {bmi}")

if bmi <18.5:
    print ("You are Underweight")
elif bmi >=18.5 and bmi <=25:
    print ("You are Normal")
elif bmi >=25 and bmi <=30:
    print ("You are Overweight")
else:
     print ("You are Obese")