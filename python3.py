age = int(input("How old are you ?\n"))

if age >= 18 :
    license = input ("Do you have a licence ?\n")

    if  license.lower () == "yes" :
        print("go ahead")
    else :
        print("park on the right")
else :
    print("park on the right")

compile