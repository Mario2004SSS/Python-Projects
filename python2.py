int_seconds = int(input("Please, enter the duration of the course with seconds :\n"))

seconds = int_seconds % 60
hours = int_seconds // 3600
minute =  ((int_seconds // 60 ) % 60 )
print(f"The entire course is : {hours} hours and {minute} minutes and {seconds} seconds")




