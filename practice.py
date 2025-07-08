print("Welcome to place the rabbit")

field = [
["🍀" , "🍀" , "🍀" ],
[ "🍀" , "🍀" , "🍀" ],
[ "🍀" , "🍀" , "🍀" ]
]
print(f"{field[0]}\n{field[1]}\n{field[2]}")
print ("Where should the rabbit go ? 🐇")
rabbit_place = input("Please choose a row and a column : ")

row = int(rabbit_place[0]) -1
column = int(rabbit_place[1]) -1
field[row][column] = "🐇"

print(f"{field[0]}\n{field[1]}\n{field[2]}")