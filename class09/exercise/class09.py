# Ex.1:Property in Python 

# Create a class with:
#   name
#   private __gpa
class Student:
    def __init__ (self,name,gpa):
        self.name=name
        self.__gpa=gpa

    @property
    def gpa (self):
        return self.__gpa ## ----> A getter cannot receive any other parameter than self and it returns something. It cannot assign a value
    
# Requirements:
#   property gpa
#   setter only accepts values between 0.0 and 4.0
    @gpa.setter
    def gpa (self,value):
        if  value >= 0.0 and value <= 4.0:
            self.__gpa=value

#-----------------------------------------------------

# Ex.2

# Create a class with:
#   name
#   internal _price
class Property:
    def __init__ (self,name, internal_price):
        self.name=name
        self.internal_price=internal_price

# Requirements:
#   property price

    @property
    def price(self):
        return self.internal_price
    
    # setter must reject negative values@price.setter
    def price(self,property_price):
        if property_price <= 0:
            print("Price rejected, please enter a positive vaue")
        else:
            self.internal_price=property_price

#---------------------------------------------------

# Ex.3 

# Create a class with:
class Circle:
#   radius
    def __init__ (self,radius):
        self.radius=radius

# Requirements:
# a read-only property area
# You should not store area directly; you should compute it.
    @property
    def area(self):
        return (self.radius ** 2) * 3.1416 

# -------------------------------------------------


# Ex.4 

# Create a class with:

class Student:
#   first_name
#   last_name
    def __init__ (self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

# Requirements:
#   read-only property full_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        



##-----------------------------------------

# Ex.5

# Create a class with:
#   owner
#   private __balance
class Client:
    def __init__ (self,owner,balance):
        self.owner=owner
        self.balance=balance

# Requirements:
#   property balance
    @property
    def balance(self):
        return self.__balance
    
#   setter prevents negative values
    @balance.setter
    def balance(self,balance):
        
        if balance < 0:
            
            print ("You cannot have an account with negative ammounts")
            self.__balance=0
        else:
            self.__balance=balance
        
        
    
           

#   method deposit(amount)
    def deposit (self,amount):
        self.__balance +=amount
        print (f"You deposited: {amount}")

#   method withdraw(amount)
    def withdraw (self,amount):
        if amount > self.__balance:
            print("You have insufficient founds")

        else:
            self.__balance-=amount
            print (f"You withdrew :{amount}  ")
# TESTING
AstridAccount=Client("Astrid",200)
AstridAccount.deposit(500)
AstridAccount.withdraw(1000)

print(AstridAccount.balance)

#-----------------------------------------
# Ex.6
class Article:

# Create a class with:
#   name
#   private __price
#   quantity
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
# Requirements:
#   property price
    @property
    def price(self):
        return self.__price
#   setter prevents negative values
    @price.setter
    def price(self,price):
        if price > 0:
            self.__price=price
        else:
            raise ValueError("Price cannot be negative")



#   read-only property inventory_value
    @property
    def inventory_value(self):
        return self.quantity *self.__price
#---------------------------------------------------------
#TESTING
article1=Article("pencil",5.99,10000)


article1.price=12.13
print(article1.price)
print(article1.inventory_value)



#--------------------------------------------------------
# Ex.7
class Movie:

# Create a class with:
#   title
#   private __rating
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating

# Requirements:
#   property rating
    @property
    def rating(self):
        return self.__rating
    
#   setter only accepts values between 0 and 10
    @rating.setter
    def rating(self,value):
        if 0 <= value <= 10:
            self.__rating=value
        else:
            
            raise ValueError ("Enter a valid number between 0 and 10")
        
##### Testing 
Movie1=Movie("Neige Blanche",10)
print(Movie1.rating)