str_length = input("Please, type length : \n")
str_width = input("please, type width : \n")
metter_cost = input("How much for 1 metter ?\n")

#Convert type
length = float(str_length)
width = float(str_width)
cost = float (metter_cost)

area = length * width
total_cost = area * cost

print("The total area is : " f"{area}")
print("The total cost is : " f"{total_cost}")


