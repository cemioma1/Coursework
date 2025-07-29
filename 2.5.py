subtotal = float(input("Enter the subtotal:"))
gratuity_rate = float(input("Enter the gratuity rate:"))
gratuity = (subtotal * (gratuity_rate / 100))
total = subtotal + gratuity
print (f"The gratuity is {gratuity}, and the total is {total}")
