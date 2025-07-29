investmentAmount = float(input( "Enter investment amount:"))
annualInterestRate = float(input ("Enter annual interest rate:"))
numberOfYears = int(input("Enter number of years:"))
#convert yearly to monthly
monthlyInterestRate = annualInterestRate / 1200
numberOfMonths = numberOfYears * 12

futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths

print (f"The accumulated value is: {futureInvestmentAmount:.2f}")