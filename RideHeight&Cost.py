height = float(input("Welcome to the ride! How tall are you? "))

if height > 5:
    age = float(input("Please specify your age: "))
    if age < 12:
        print("You will be paying $5")
    elif age <= 18:
        print("You will be paying $7")
    elif age > 18:
        print("You will be paying $12")

else:
    print("I am sorry, but you are not tall enough to ride.")


