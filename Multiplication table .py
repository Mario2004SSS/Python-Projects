print(" **** Welcome to the multiplication table ****")

number = int(input("Enter a number : "))
print (f"Multiplication table for {number} : ")
for i in range (1,11) :

    print (f"{number} x {i} = {number*i}")




print("Welcome")
list_a = []
friends_list = input("Enter the first and last name of your friends seperated by a comma: ").split(", ")
lenth = len(friends_list)
for i in range(0 , lenth) :
    x = friends_list[i]
    y = x.split(" ")
    print(y)
    list_a.append(y)

    print(y[0][0], "." , y[1][0],".")
    
print(list_a)
    