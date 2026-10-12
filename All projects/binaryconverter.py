num=float(input("Enter a number: "))
decimal = round(num) - num
whole = int(num)

binary_whole = bin(whole)[2:0]
binary_decimal = ""

while decimal != 0:
    New_decimal=decimal*2
    if New_decimal*2 > 1:
        binvalue_decimal=0
    else:
        binvalue_decimal=1
    binary_decimal += str(binvalue_decimal)
    decimal = New_decimal - binvalue_decimal

print(f'Binary value of {num} is {binary_whole}.{binary_decimal}')
