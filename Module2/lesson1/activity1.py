

medical_cause = str(input("Did you have a medical cause? (Y/N): ")).upper().strip()
if medical_cause == 'Y':
    print("You are allowed to attend the exam.")
elif medical_cause == 'N':
    atten = int(input("What is your attendance percentage? (0-100): "))
    if atten >= 75:
        print("You are allowed to attend the exam.")
    else:
        print("You are not allowed to attend the exam.")