print("Welcome to 'Whose wallet?'")
print("You will give me a list of names, and I will pick a person to pay")
names_sep = input("If you are ready, enter the names seperated by a comma : ")
names = names_sep.split(", ")
import random
x = len(names)-1

shose = random.randint (0,x)
print(f"Please ask ' {names [shose]} ' to take his wallet out. Dinner is on him")