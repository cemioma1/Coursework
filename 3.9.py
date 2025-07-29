employee_name = str(input("Enter employees name:"))
hours_worked =(float(input("Enter number of hours worked in a week:")))
pay_rate = float(input("Enter hourly pay rate:"))
gross_pay = (hours_worked * pay_rate)
federal_tax = float(input("Enter federal tax withholding rate:"))
federal_withholding = pay_rate * federal_tax
state_tax = float(input("Enter state tax withholding rate:"))
state_withholding = (pay_rate * state_tax)
deductions = federal_tax + state_tax
net_pay = (pay_rate * hours_worked) - deductions
print (f"Employer Name:${employee_name}")

print (f"Hours Worked:${hours_worked:.2f}")
print (f"Pay Rate:${pay_rate:.2f}")
print ("Deductions:")
print (f"Federal Withholding: ${federal_tax:.2f}")
print (f"State Withholding:${state_tax:.2f}")
print (f"Net Pay: ${net_pay:.2f}")
