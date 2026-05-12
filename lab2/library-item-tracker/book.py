class Book:
    library_name="Central Library"
    count=0
    def __init__(self,title,author,available,genre):
        self.title=title
        self.author=author
        self.available=available
        self.genre=genre
        Book.count+=1

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
        print(f"Title:{self.title}, author:{self.author}, availability:{self.available},genre:{self.genre}" )

    @classmethod

    def show_count(cls):
        print(f"You have been created {cls.count} books")

    @classmethod
    def from_string(cls,data):
        title, author, available,genre=data.split(",")
        return cls(title,author,available,genre)