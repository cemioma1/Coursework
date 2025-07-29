
today = eval(input("Enter today's day:( 0 for sun, 1 for mon, 2 for tue...."))
days_passed = eval(input("Enter the number of days elapsed since today:"))
futureDays = (today + days_passed) % 7

#current day and day of the week
if today == 0:
    weekDay = ("Sunday")
elif today == 1:
    weekDay = ("Monday")
elif today == 2:
    weekDay = ("Tuesday")
elif today == 3:
    weekDay = ("Wednesday")
elif today == 4:
    weekDay = ("Thursday")
elif today == 5:
    weekDay = ("Friday")
elif today == 6:
    weekDay = ("Saturday")
#number of days passed and what day it landed on
if futureDays == 0:
    futureDay = ("Sunday")
elif futureDays == 1:
    futureDay =("Monday")
elif futureDays == 2:
    futureDay =("Tuesday")
elif futureDays == 3:
    futureDay =("Wednesday")
elif futureDays == 4:
    futureDay = ("Thursday")
elif futureDays == 5:
    futureDay = ("Friday")
elif futureDays == 6:
    futureDay = ("Saturday")
print (f"Today is {weekDay} and the future day is {futureDay}")
todaysDay = eval(input("Enter today's day:"))
days_passed2 = eval(input("Enter the number of days elapsed since today:"))
print (f"Today is {weekDay} and the future day is {futureDay}")