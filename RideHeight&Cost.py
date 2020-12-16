print("Welcome to the roller coaster ride!")
print("\n")
height = float(input("How tall are you? "))
bill = 0
if height > 4.5:
    age = float(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Your ticket will be $5")
    elif age <= 18:
        bill = 7
        print("Your ticket will be $7")
    else:
        bill = 12
        print("Your ticket will be $12")

    picture = str(input("Would you like to add $3 for a picture? yes or no "))
    if picture == "yes":
       bill += 3
    print(f"Your final will be ${bill}")

else:
    print("Sorry, but you are not tall enough to ride.")

