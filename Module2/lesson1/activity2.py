Electricity_Units=int(input("Enter the number of electricity units consumed: "))

if Electricity_Units<50:
    bill_amount= Electricity_Units*2.6+25
    print("Your bill amount is: ",bill_amount)
elif Electricity_Units>=50 and Electricity_Units<100:
    bill_amount= Electricity_Units*3.25+35
    print("Your bill amount is: ",bill_amount)
elif Electricity_Units>=100 and Electricity_Units<200:
    bill_amount= Electricity_Units*5.26+45
    print("Your bill amount is: ",bill_amount)
else:
    bill_amount= Electricity_Units*8.45+75
    print("Your bill amount is: ",bill_amount)