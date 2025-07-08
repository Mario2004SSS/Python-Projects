print("Welcome to the Rock, Paper, Scissors game:")
import random
user_input = input("Press Enter to continue or type (Help) for the rules help : ").capitalize()
if user_input :
     print("")  



if  user_input == "Help":

     print("            ************** RULES **************")
     print("            1) Yoy choose and the computer chooses")
     print("            2) Rock smashes Scissors ⇒ Rock wins")
     print("            3) Scissors cut paper ⇒ Scissors wins")
     print("            4) Paper covers Rock ⇒ Paper wins")






Rock = ("""
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")





Paper = ("""    
     ______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""     
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)               
 """)

import random
gamelist = ["Rock", "Paper" , "Scissors"]
computer_input = random.choice(gamelist)
user_choice = input("Enter your choice (Rock, Paper, Scissors) : ").capitalize()
if computer_input in gamelist :
    print("")
    if user_choice == computer_input  :
        print("draw")
        if user_choice == gamelist[0] :
            print("You chose")
            print(Rock)
            print("Computer chose")
            print(Rock)
            print("Draw")
        elif user_choice == gamelist[1] :
            print("You chose")
            print(Paper)
            print("Computer chose")
            print(Paper)
            print("Draw")
        else :
            print("You chose")
            print(Scissors)
            print("Computer chose")
            print(Scissors)
            print("Draw")
    elif user_choice == "Rock" and computer_input == "Paper" :
        print("You chose")
        print(Rock)
        print("Computer chose")
        print(Paper)
        print("You lost : Paper covers Rock")

    elif user_choice == "Rock" and computer_input == "Scissors" :
        print("You chose")
        print(Rock)
        print("Computer chose")
        print(Scissors)
        print("You wan : Rock smashes Scissors")
    
    elif user_choice == "Paper" and computer_input == "Rock" :
        print("You chose")
        print(Paper)
        print("Computer chose")
        print(Rock)
        print("You wan : Paper covers Rock")
    elif user_choice == "Paper" and computer_input == "Scissors" :
        print("You chose")
        print(Paper)
        print("Computer chose")
        print(Scissors)
        print("You lost : Scissors cuts Paper")
    elif user_choice == "Scissors" and computer_input == "Rock" :
        print("You chose")
        print(Scissors)
        print("Computer chose")
        print(Rock)
        print("You lost : Rock smashes Scissors")
    elif user_choice == "Scissors" and computer_input == "Paper" :
        print("You chose")
        print(Scissors)
        print("Computer chose")
        print(Paper)
        print("You wan : Scissors cuts Paper")        

    else :
        print("ss")
else :
     print("Invalid Input")