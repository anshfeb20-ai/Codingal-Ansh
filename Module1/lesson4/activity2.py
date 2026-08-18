amount=int(input("Enter your amount: "))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("100 notes: ",note_1)
print("50 notes: ",note_2)
print("10 notes: ",note_3)
