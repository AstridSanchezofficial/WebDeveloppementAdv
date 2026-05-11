class Book:
    counter=0
    def __init__(self, book_name,author,year):
        self.book_name=book_name
        self.author=author
        self.year=year
        Book.counter =+1

class Student:

    school_name="Vanier College"
    student_count=0

    def __init__(self,name,program,grade):
        self.name=name
        self.program=program
        self.grade=grade
        Student.student_count=+1

    def display_info(self):
        print(f"Alice studies {self.program} at {self.school_name}. Grade: {self.grade}")

student1=Student("Astrid","Computer Science",8)
student1.display_info()


class Product:
    tax_rate=0.15
    category="Electronics"


    def __init__(self,name,price):
        self.name=name
        self.price=price

    def price_with_tax(self):
       return self.price+(self.price*self.tax_rate)
    
    def print_product(self):
        print(f"Product: {self.name},Price:{self.price_with_tax()}")

product1=Product("computer",450)
product1.print_product()
Product.tax_rate=0.20
product1.print_product()

class Employee:
    company_name="TechNova"
    bonus_rate=0.10
    employee_count=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_bonus(self):
        return self.salary*self.bonus_rate
    
    def display_info(self):
        print(f"{self.name} works at {self.company_name}. Salary:{self.salary}. Bonus:{self.calculate_bonus()} ")

employee1=Employee("Carla",23000)
employee2=Employee("Daniel",100000)
employee1.display_info()
employee2.display_info()

Employee.bonus_rate=0.20

employee1.display_info()
employee2.display_info()

#Employee 1 has a shadowed bonus 
employee1.bonus_rate=0.50
employee1.display_info()

Employee.bonus_rate=0.05
employee1.display_info()
employee2.display_info()



        
    
