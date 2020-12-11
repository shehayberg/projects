print("Curious to find out how many weeks you have left to live if you made it to 90 years old...? Let's find out!\n\n")

age = input("Please provide me your age: ")
age_as_int = int(age)
years_left = (90 - age_as_int)
months_left = (12 * years_left)
weeks_left = (52 * years_left)
days_left = (365 * years_left)

message = f"You have: {days_left} days, {weeks_left} weeks, {months_left} months, and {years_left} years left of your life."

print(message)

