from abc import ABC, abstractmethod
#ABSTRACT CLASSES AND METHOD CLASSES

#Implement a basic notification system

#1. I WANT AN INTERFACE /abstract class of notification
#abstract method ---> send (self,message)

class Notification(ABC):
    @abstractmethod
    def send(self,message):
        pass

#2. CONCRETE IMPLEMANTATION OF THIS CLASS

#Email notification Class
class Email(Notification):
    def send(self,message,email):
    
        print(f"Sending message by email:{message} to {email} ")
    
#SMS notification Class
class Sms(Notification):
    def send(self,message,phone):
        print(f"Sending SMS: {message} to {phone}")


#3. THEN USE THEM HERE 

def notify(message, type_of_message , send_to):
    if type_of_message=="Sms":
        sms=Sms()
        sms.send(message,send_to)
    elif type_of_message=="Email":
        email=Email()
        email.send(message,send_to)

    else:
        print("Choose the type of message (Email or Sms)")


notify("Whats up?", "Sms", 17647357436)
notify("I hope you are doing okak", "post","jorge.sama@yahoo.com")


##Solucion 2

    