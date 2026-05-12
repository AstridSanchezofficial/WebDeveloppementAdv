from book import Book


book1=Book("Ux design","Karine Allemand", False, "Ux design")
book2=Book("Human-Computing Intercation", "Joseph Collins", True, "Tech") 
book3=Book("","Oscar Wild",False,"Science Fiction")

book1.return_book()
book1.borrow()
book1.display_info()
#Testing STATIC AND CLASS METHODS
print(Book.library_name)

#Changing the library
Book.change_library_name("Coop Ets")
print(Book.library_name)

##Validating the title
Book.is_valid_title(book3.title)
Book.is_valid_title(book2.title)

##Printing book with genre 
book2.display_info()