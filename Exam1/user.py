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

class VipCustomer(Customer):
    def __init__(self,name,email,customer_id,level):
        super().__init__(name,email,customer_id)
        self.level=level
    def display_info(self):
        print(f'User: {self.name} |level:{self.level} |customer id: {self._Customer__customer_id} | email: {self.email}')
    
