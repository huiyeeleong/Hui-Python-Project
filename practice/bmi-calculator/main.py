
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = weight / (height*height)
bmi = int(bmi)

if bmi <= 18:
  print("Your BMI is " + str(bmi) + ", you are underweight")

elif bmi < 25:
  print("Your BMI is " + str(bmi) + ", you have a normal weight")

elif bmi < 30:
  print("Your BMI is " + str(bmi) + ", you are slightly overweight.")

elif bmi < 35:
  print("Your BMI is " + str(bmi) + ", you are obese.")

else:
  print("Your BMI is " + str(bmi) + ", you are clinically obese.")
