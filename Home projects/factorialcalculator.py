factorial=int(input("Enter a number: "))
i=0
num=1

while i<factorial:
    num=num*(factorial-i)
    i+=1

print("The factorial of", factorial, "is", num)