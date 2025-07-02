
color_list = ["Red" , "Blue" , "White" , "Black" , "Green" , "Yellow" , "Orange" , "Purple" , "Brown" , "Gray" , "Beige" , "Pink" , "Gold" , "Silver"]

my_favorite_colors = [ ]
first_color = input("Add the first color you like:  ").capitalize()
if first_color in color_list :
    my_favorite_colors.append(first_color)
    choice = input("Do you want to add more colors ? type (yes) or (no)\n").lower()
    if choice == "yes" :
        second_color = input("Add another color to the list: ")
    
        my_favorite_colors.append(second_color)
        print(my_favorite_colors)
    elif choice == "no" :
         print(my_favorite_colors)
    else :
        print("Invalid input")
else :
    print("Invalid input")
