print("Welcome to tip calculator")
val = float(input("What was the total bill?"))
number = int(input("How many people to split the bill?"))
bill_per_person = val / number
tip_per_person = int(input("Percentage of tip per person?"))
total_bill_per_person = bill_per_person * (tip_per_person)/100  + bill_per_person
print("Each person should pay: $"+str(total_bill_per_person))


