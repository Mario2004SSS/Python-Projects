print ("Welcome to place the rabbit")
rabbit_game = [

[ "🍀" , "🍀" , "🍀" ],
[ "🍀" , "🍀" , "🍀" ],
[ "🍀" , "🍀" , "🍀" ]

]
print ( rabbit_game[0])
print ( rabbit_game[1])
print ( rabbit_game[2])

print ("Where should the rabbit go ? 🐇")
rabbit_place = input("Please choose a row and a column : ")
rabbit = "🐇"
row = int(rabbit_place[0]) -1
column = int(rabbit_place[1]) -1
if row == 0 :
    rabbit_game[0].remove("🍀")
    rabbit_game[0].insert(column , rabbit )
    print ( rabbit_game[0])
    print ( rabbit_game[1])
    print ( rabbit_game[2])
elif row == 1 :
    rabbit_game[1].remove("🍀")
    rabbit_game[1].insert(column , rabbit)
    print ( rabbit_game[0])
    print ( rabbit_game[1])
    print ( rabbit_game[2])
elif row == 2 :
    rabbit_game[2].remove("🍀")
    rabbit_game[2].insert(column , rabbit )
    print ( rabbit_game[0])
    print ( rabbit_game[1])
    print ( rabbit_game[2])


else :
    print(f"Your choice is not correct")

