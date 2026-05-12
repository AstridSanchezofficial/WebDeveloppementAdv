class Book:
    library_name="Central Library"
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available

    @classmethod
    def change_library_name(cls,new_library):
       cls.library_name = new_library        
        
    @staticmethod

    def is_valid_title(title):
        if title =="":
             print("Invalid title, try again")
        else:
            print("Valid title")
    def borrow(self):
        self.available=False

    def return_book(self):
        self.available=True
    
    def display_info(self):
        print(f"Book's name:{self.title}, author:{self.author}, availability:{self.available}")
