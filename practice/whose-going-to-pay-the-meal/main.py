import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Calculate the number of the names
num_items = len(names)

#Random the number of the names
random_the_name = random.randint(0, num_items - 1)

#Prompt the random name

person_who_pay = names[random_the_name]
print(f"{person_who_pay} is going to buy the meal today")