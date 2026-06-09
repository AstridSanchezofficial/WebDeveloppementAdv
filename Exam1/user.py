# PART 3 -INHERITANCE
class User():
    def __init__(self,name,email):
        self.name=name
        self.email=email
    # Method display_info()
    def display_info(self):
        print (f'User: {self.name} | email: {self.email}')
# Creating Child classes
class Customer(User):
    def __init__(self,name,email,customer_id):
        super().__init__(name,email)
        self.__customer_id=customer_id
    def display_info(self):
        print(f'User: {self.name} | customer id: {self.__customer_id} | email: {self.email}')
    
class Staff(User):
    def __init__(self,name,email,employee_id):
        super().__init__(name,email)
        self.__employee_id=employee_id
    def display_info(self):
        print(f'User: {self.name} | employee id: {self.__employee_id} | email: {self.email}')
    
# user1=User('astrid',"astrid@gmail.com")
# user1.display_info()

# user2=Customer('Daniela',"dani@gmail.com",1)
# user2.display_info()

# user3=Staff('Ogenchi',"ogenchi@gmail.ca",2)
# user3.display_info()
