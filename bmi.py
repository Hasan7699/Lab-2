the_height = float(input("Enter the height in cm: "))
the_weight = float(input("Enter the weight in kg: "))
the_BMI = the_weight / (the_height/100)**2
print("Your Body Mass Index is", the_BMI)
if the_BMI <= 18.5:
    print("Oops! You are underweight.")
elif 18.5<=the_BMI <= 25:
    print("Awesome! You are healthy.")
elif the_BMI <= 30:
    print("Eee! You are overweight.")
else:
    print("Seesh! You are obese.")