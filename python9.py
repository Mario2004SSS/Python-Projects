import random
full_list = [ 0 , 1 , 2 , 3 , 4 , 5 ]
computer_shose = random.randint (0 , 5)
user_input = int(input("Enter a number between 0-5 :"))
if user_input == computer_shose :
    print("you passed the first level")
    full_list.remove (computer_shose)
    user_input = int(input("Enter a number between 0-5 :"))
    computer_shose = random.choice (full_list)
    if user_input == computer_shose :
        print("you passed the second level")

        full_list.remove (computer_shose)
        user_input = int(input("Enter a number between 0-5 :"))
        computer_shose = random.choice (full_list)
        if user_input == computer_shose :
            print("you passed the third level")

            full_list.remove (computer_shose)
            user_input = int(input("Enter a number between 0-5 :"))
            computer_shose = random.choice (full_list)
            if user_input == computer_shose :
                print("you passed the fourth level")

                full_list.remove (computer_shose)
                ser_input = int(input("Enter a number between 0-5 :"))
                computer_shose = random.choice (full_list)
                if user_input == computer_shose :
                    print("Congarruation! you win the game")
                else :
                    print(f"Game over , The computer entered {computer_shose}")
            else :
                print(f"Game over , The computer entered {computer_shose}")
        else :
            print(f"Game over , The computer entered {computer_shose}")
    else :
        print(f"Game over , The computer entered {computer_shose}")
else :
    print(f"Game over , The computer entered {computer_shose}") 
