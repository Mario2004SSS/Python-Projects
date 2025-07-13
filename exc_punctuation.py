user_input = input("Please type a sentence : ")
import string
for letter in user_input :
    if letter in string.punctuation :
       
       user_input = user_input.replace(letter , '')
    else :
       user_input = user_input

print( user_input )