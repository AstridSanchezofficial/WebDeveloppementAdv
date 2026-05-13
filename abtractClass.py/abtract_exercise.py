# 1. Create an abstract class:
from abc import ABC, abstractmethod

# Vehicle

class Vehicule(ABC):

# abstract method: move()
    @abstractmethod
    def move(self, speed):
        pass

# Create subclasses:
# Each must implement move() differently
# Car

class Car(Vehicule):
    def move(self,speed):
        print(f"The car moves at {speed}km/h")
# Bicycle
class Bicycle(Vehicule):
    def move(self,speed):
        print(f"The bicycle moves at {speed}km/h")

#Implementation


def display_speed(vehicule, speed):
    vehicule.move(speed)
    
vehicule1=Car()
vehicule2=Bicycle()
    
display_speed(vehicule1,200)
display_speed(vehicule2,50)


# 2. Create an abstract class:
print("--------------")
# FileHandler
class FilHandler(ABC):
    #abstract methods: 

# read()
    @abstractmethod
    def read(self,message):
        pass
# write()
    @abstractmethod
    def write(self):
        pass
# Create subclasses:
# TextFileHandler
class TextFileHandler(FilHandler):

    def read (self,message):
        print("Reading message..")
        print(f" Here is the TEXT message: {message}")

    def write(self,message):
        print(f"Typing text message:`{message}`")
        

# JsonFileHandler
class JsonFileHandler(FilHandler):
    def read(self,message):
        print("Reading message")
        print(f"Here is the JSON message:{message}")

    def write(self,message):
        print(f"Typing JSON message {message}")

#Implementing 

# They can just print messages instead of reading real files.
def read_file(File_type,message):
    File_type.read(message)

def write_file(File_type,message):
    File_type.write(message)

json_file=JsonFileHandler()
text_file=TextFileHandler()


read_file(json_file,"name:Astrid,grade:3rd")
write_file(text_file,"There is 5 types of organic elements")



# 3. Create an abstract class:
# Account
class Account (ABC):
    # abstract method: calculate_fee()
    @abstractmethod
    def calculate_fee(self,ammount):
        pass

# Create subclasses:

# SavingsAccount
class SavingAccount(Account):

    def calculate_fee(self,ammount):
        fee=0.05*ammount
        return fee
        

# PremiumAccount

class PremiumAccount(Account):
    def calculate_fee(self,ammount):
        fee=0.005*ammount
        return fee

# Each returns a different fee.
#Implementing the method
def display_fee(account_type,ammount):
    print(account_type.calculate_fee(ammount))

account1=PremiumAccount()
account2=SavingAccount()

display_fee(account1,10000)
display_fee(account2,10000)




# 4. abstract Employee
# Create:
# abstract class Employee

class Employee(ABC):

# abstract method calculate_salary()
    @abstractmethod
    def calculate_salary(self,rate):
        pass
# Subclasses:
# FullTimeEmployee
class FullTimeEmployee(Employee):
    hours=40
    def calculate_salary(self, rate):
        total_payment=self.hours*rate
        print(f"As a Fulltime employee your salary is:{total_payment}")
# PartTimeEmployee

class PartTimeEmployee(Employee):
    hours=20
    def calculate_salary(self,rate):
        total_payment=self.hours*rate
        print(f"As a Part-time employee your salary is:{total_payment}")

# Each should calculate salary differently.
def get_salary (employe_type, rate_hour):
    employe_type.calculate_salary(rate_hour)

employee1=PartTimeEmployee()
employee2=FullTimeEmployee()

get_salary(employee1,20)
get_salary(employee2,24)

# 5. abstract Media
class Media(ABC):
    @abstractmethod
# abstract method play()
    def play(self,file):
        pass

# Subclasses:
# Song
class Song(Media):
    def play(self,file):
        print(f"Playing ... {file}")

# Video
class Video(Media):
    def play(self,file):
        print(f"Streaming ... {file}")

# Each implements play() differently.
def ready(media_type,file):
    media_type.play(file)

video1=Video()
song1=Song()

ready(video1,"Best skincare brands")
ready(song1,"Allucinate")