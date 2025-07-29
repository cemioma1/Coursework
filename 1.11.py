'''(Population projection) The US Census Bureau projects population based on the
following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days. Hint: in Python, you
can use integer division operator // to perform division. The result is an integer. For
example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5)'''


currentPopulation = 312032486
print (currentPopulation)
rate =  (365 * 24 * 60 * 60)//7 + (365 * 24 * 60 *
60)//45 - (365 * 24 * 60 * 60)//13
print (rate)

year1 = (currentPopulation + rate)
print (year1)
year2 = (year1 + rate)
print (year2)
year3 = (rate + year2)
print (year3)
year4 = (year3 + rate)
print (year4)
year5 = (year4 + rate)
print (year5)
