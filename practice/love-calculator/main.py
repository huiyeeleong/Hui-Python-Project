#Input
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Calculate the word
name_count = name1 + name2
lower_cap = name_count.lower()
t = lower_cap.count("t")
r = lower_cap.count("r")
u = lower_cap.count("u")
e = lower_cap.count("e")

first_letter = t + r + u + e

l = lower_cap.count("l")
o = lower_cap.count("o")
v = lower_cap.count("v")
e = lower_cap.count("e")

second_letter = l + o + v + e

#Total Score
total_score = int(str(first_letter)+ str(second_letter))

#Statement
if (total_score <= 10) or (total_score >= 90):
  print(f"Your score is {total_score}, you go together like coke and mentos.")

elif (total_score >= 40) or (total_score <=50):
  print(f"Your score is {total_score}, you go together like coke and mentos")

else:
  print(f"Your score is {total_score}")









