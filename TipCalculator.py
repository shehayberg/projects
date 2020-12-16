print("*" * 30)
print("Welcome to the tip calculator")
print("*" * 30)

bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

tip_amount = ((percentage / 100) * bill)
split_amount = round((bill / people) + tip_amount,2)

print(f" Each person should pay ${split_amount} ")




















