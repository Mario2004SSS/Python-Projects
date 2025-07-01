natinality = input("Are you libyan? type ( yes ) or ( no ) : ").lower()

if natinality == "yes" :
    age = input("Are you above 18 ? type ( yes ) or ( no ) : ").lower ()
    if age >= "yes" :
        print(" you can get an ID ")
    else :
        print (" Sorry,your age at least must be 18 ")
elif natinality == "no" :
    print(" Libyan ID is only for Libyan ")
else :
    print(f" your entery {natinality} is not defined ")



