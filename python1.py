print("Welcome to my application")
age = int(input("How old are you ?\n"))

if age >= 10 :
    print("Good. you can use the app")
    number = float(input("Enter a number :\n"))

    if number > 0 :
        print ("The number is +ve")
    elif number < 0 :
        print("The number is -ve")
    else :
        print(" The number is zero")

else :
    print("Sorry, you can't use the app")

