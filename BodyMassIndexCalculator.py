print("*" * 47)
print( "Welcome to the free body mass index calculator")
print("*" * 47)

print("Would you like to figure out where you stand in terms of health? If so, let's get started!")
print("\n")

height = float(input("Please enter your approximate height in Feet: "))
weight = float(input("Pleas enter your approximate weight in Pounds: "))
print("\n")

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print("You are considered underweight. Please speak to your doctor about it!")
elif bmi < 25:
    print("You are considered to have a normal weight. Good job!")
elif bmi < 30:
    print("You are considered overweight. Please speak to your doctor about it.")
else:
    print("You are considered obese. Please urgently speak to your doctor about it!")


