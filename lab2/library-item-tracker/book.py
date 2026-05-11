class Book:
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available

    def borrow(self):
        self.available=False

    def return_book(self):
        self.available=True
    
    def display_info(self):
        print(f"Book's name:{self.title}, author:{self.author}, availability:{self.available}")
