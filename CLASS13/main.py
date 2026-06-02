# 1
# Create a parent class:
#   Animal
class Animal():
    ##In this case we do not need to create the constructor cause we are not assigning any value we are just printing some data here 

#   method: speak()
    def speak(self):
        print(f"I am a {self.type} animal")
# then child classes:
# Override speak in ceach child!

# Dog says "Woof"
# Cat says "Meow"
#   Dog
class Dog(Animal):
   
    def speak(self):
        print("Woaf")
#   Cat

class Cat (Animal):
    def speak(self):
        print("Miau")

animals=[Cat(),Dog(),Dog()]

for animal in animals:
    animal.speak()

# Then loop through them polymorphically


# 2
# Create a parent class: Vehicle
# the share 
# brand
# describe()
class Vehicule():
    def __init__(self,brand):
        self.brand=brand
    def describe(self):
        print(f"The brand is {self.brand}")

# Child classes Car and Bike
# add child-specific behaviour
class Car(Vehicule):
    def __init__(self,brand,type="car"):
        super().__init__(brand)
        self.type=type
    
    def describe(self):
        print(f"This is a  {self.type} and the brand is {self.brand} ")

class Bike(Vehicule):
    def __init__(self,brand,type="bike"):
        super().__init__(brand)
        self.type=type
    
    def describe(self):
        print(f"This is a  {self.type} and the brand is {self.brand} ")

vehicules=[Vehicule("Ford"),Car("Ferarri"),Bike("Bike Mountain")]

for vehicule in vehicules:
    vehicule.describe()



# 3
# parent class: Account
#               show_type()
class Account():
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name

    def show_type(self):
        print(f"{self.name} {self.last_name} has a regular account")

# children accounts: SavingsAccount & PremiumAccount
#   override or extend behaviour accordingly
class SavingAccount(Account):

    def __init__(self,name,last_name,rate):
        super().__init__(name,last_name)
        self.rate=rate
    def show_type(self):
        print(f"{self.name} {self.last_name} your savings account has the following rate:{self.rate}")

class PremiumAccount(Account):
    def __init__(self,name,last_name,account_level):
        super().__init__(name,last_name)
        self.account_level=account_level
    def show_type(self):
        print(f"{self.name} {self.last_name} your premium account level is: {self.account_level}")

accounts=[Account("Astrid","Sanchez"),SavingAccount("Daniela","Perez",8),PremiumAccount("Iker","Casillas","Silver")]

for account in accounts:
    account.show_type()