number=int(input("Enter a number: "))
sum=0
temp=number
p=len(str(number))
while number>0:
    digit=number%10
    sum=sum+(digit**p)
    number=number//10
if sum==temp:
    print(temp," is an Armstrong Number")
else:
    print(temp," is not an Armstrong Number")
