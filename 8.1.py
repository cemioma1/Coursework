ssn = str(input("Enter Social Security Number in format ddd-dd-dddd:  "))

if len(ssn) ==[3]=='-'  and ssn [6]=='-' and ssn [:3].isdigit() and ssn [4:6].isdigit() and ssn [7:].isdigit():
    print("Valid SSN")

else:
    print("Invalid SSN")

