pounds = float(input("enter your weight in pounds: "))
inches = float(input("enter youre height in inches: "))

bmi = pounds / (inches * inches)

print("your bmi is: ", bmi)

kilagram = 0.453592 * pounds
meters = 0.0254 * inches
if kilagram is bmi <= 18.5:
    print("you are uderweight")

if kilagram is 18.5 <= bmi < 24.9:

    print("you are normal weight")
if kilagram is 25 <= bmi < 29.9:

    print("you are overweight")
if kilagram is bmi >= 30:

    print("you are obese")
