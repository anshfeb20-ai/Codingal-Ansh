integer1=int(input("Enter an integer: "))
i=0
product=1
while i < integer1:
    product=product*(integer1-i)
    i=i+1
print(product)
