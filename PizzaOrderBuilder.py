print("*" * 70)
print("Welcome to the Python Pizza Shop! Shall we get started on your order?")
print("*" * 70)
print("\n")

#small = $10
#medium = $15
#large = $20
#small pepperoni = $2
#medium & large pepperoni = $3
#xtra cheese = $1

bill = 0

pizza_size = input("What size pizza would you like to order today: S, M, or L? ")
if pizza_size == "S":
    bill = 10

elif pizza_size == "M":
    bill = 15

elif pizza_size == "L":
    bill = 20

print("\n")

add_pepperoni = input("Would you like to add pepperoni onto your pizza? Y or N? ")
if pizza_size == "S":
    bill += 2
else:
    bill += 3

print("\n")

add_cheese = input("Would you like to add extra cheese to your pizza? Y or N? ")
if add_cheese == "Y":
    bill += 1

print("\n")

print(f"Your total bill for today will be ${bill}")

