l=int(input("Enter the first value of the range: "))
h=int(input("Enter the second value of the range: "))
lis=[]
for num in range(l,h+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            lis.append(num)
            print(num)
    else:
        print("Please enter a number greater than 1")
print(lis)