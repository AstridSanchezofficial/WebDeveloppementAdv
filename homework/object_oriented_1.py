class Playlist:
    def __init__(self, name, song_count=0 ):
        self.name= name
        self.song_count= song_count
    
    def add_song(self):
        self.song_count+=1
        return self.song_count
    
    def remove_song(self):
        self.song_count-=1
        return self.song_count
    
    def show_info(self):
        print( f"Name of the Playlist:{self.name}  , total of songs:{self.song_count}")

#TEST ADD AND REMOVE SONG

Playlist1=Playlist("pop_latino")
Playlist1.add_song()
Playlist1.add_song()
Playlist1.add_song()
Playlist1.remove_song()
Playlist1.show_info()
     
#END

class ShoppingCart:

    def __init__(self, owner, item_count=0):
        self.owner=owner
        self.item_count=item_count
    
    def add_item(self):
        self.item_count+=1
     
    
    def remove_item(self):
        self.item_count-=1

    def show_cart(self):
        print(f"HI {self.owner} your cart has {self.item_count} items")

#TEST SHOPING CART 

shoppingCart1=ShoppingCart("Melissa")

shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.add_item()
class ShoppingCart:

    def __init__(self, owner, item_count=0):
        self.owner=owner
        self.item_count=item_count
    
    def add_item(self):
        self.item_count+=1
     
    
    def remove_item(self):
        self.item_count-=1

    def show_cart(self):
        print(f"HI {self.owner} your cart has {self.item_count} items")

#TEST SHOPING CART 

shoppingCart1=ShoppingCart("Melissa")

shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.add_item()
shoppingCart1.remove_item()
shoppingCart1.show_cart()

#END

class UserAccount:
    def __init__(self, username,login_count=0,active_state="deactivated"):
        self.username=username
        self.active_state=active_state
        self.login_count=login_count

    def activate(self):
        if self.active_state=="deactivated":
            self.active_state="activated"

    def deactivated(self):
        if self.active_state=="activated":
            self.active_state="deactivated"
        
    def login(self):
        self.login_count+=1
    
    def show_status(self):
        print(f"Hi {self.username}! your account is {self.active_state}")
        print(f"{self.username}! you have logged in {self.login_count} times")

#TEST ACCOUNT 

Account1=UserAccount("Itzel")
Account1.activate()
Account1.login()
Account1.login()
Account1.login()
Account1.login()
Account1.login()
Account1.login()
Account1.login()
Account1.login()
Account1.login()
Account1.show_status()
Account1.deactivated()
Account1.show_status()


        