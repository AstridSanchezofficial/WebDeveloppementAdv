from movieshow import MovieShow
from user import User,Customer,Staff
from status import ShowStatus




# PART 7- Polymorphism and creating valid users(part 8)
user1=User("Mathieu","mathieuw@gmail.com")
customer1=Customer("Daniela","dani@gmail.com",1)
employee1=Staff("Corey","corey@yahoo.com",2)

user1.display_info()
customer1.display_info()
employee1.display_info()

# PART 8 
# Create valid movie Show
movie1=("The Devil",100,50,ShowStatus.OPEN)
movie1.book_tickets(customer1,20)
movie1.display_info()
