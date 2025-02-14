med_cause = input("Do you have a medical cause Y or N")
attend_per = int(input("What is your attendance percentage"))
if med_cause == "Y":
    print("Allowed")
else:
    if attend_per > 75:
        print("allowed")
    else:
        print(" not allowed")
