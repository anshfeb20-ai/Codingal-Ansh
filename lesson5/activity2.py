actual=float(input("Enter the actual value: "))
sale=float(input("Enter the sale value: "))
if sale>actual:
    amount=sale-actual
    print("The profit is",amount)
else:
    print("No profit")