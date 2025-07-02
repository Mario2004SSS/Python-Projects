
library_list = [ ]
my_book = input("Enter the name of a book you own :")
library_list.append (my_book)
my_book_1 = input("Enter the name of another book you own ( or press 'Enter' to skip) :").capitalize ()
if my_book_1 :
    library_list.append( my_book_1)
    wish_list = [ ]

    wish_book = input("Enter the name of a book you wish to have in the future :").capitalize ()
    wish_list.append (wish_book)
    wish_book_2 = input("Enter the name of another book you wish to have ( or press 'Enter' to skip) :").capitalize()
    if wish_book_2 :
        wish_list.append ( wish_book_2 )
        print (f"Your Wishlist {wish_list}")
        acq_book = input("Enter the name of a book from your wishlist that you've acquired ( or press 'Enter' to skip) :").capitalize ()

        if acq_book in wish_list :
            library_list.append (acq_book)
            print(f"Updated Library : {library_list}")
            wish_list.remove (acq_book)
            print(f"Updated Wishlist : {wish_list}")
            donate_book = input("Enter the name of a book in your library you wish to donate ( or press 'Enter' to skip ) :").capitalize ()
            if donate_book in library_list :
                library_list.remove (donate_book)
                print( f"Final Library after Donations : {library_list}")
            else :
                print ("This book is not on your library_list")
                print (f"Your wishlist : {wish_list}")

        else :
            print("This book is not on your wishlist")
            print(f"Your Wishlist : {wish_list}")
            

            
        


    else :
         print (f"Your Wishlist {wish_list}")   
        

else :

    print(f"Your Library : {library_list}")