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
movie1=MovieShow("The Devil",100,50,ShowStatus.OPEN)
# Booking valid tickets
movie1.book_tickets(customer1,5)
# Display update information
movie1.display_info()


print("-----------------")
        # INVALID OPERATIONS
# Booking tooo many tickets
try:
    movie2=MovieShow('Barbie',90,60,ShowStatus.OPEN)
    movie2.book_tickets(customer1,40)
except Exception as e:
    print(f'{e} - {type(e).__name__}')

#Booking a Sold Out show

try:
    movie3=MovieShow('Fairy',30,30,ShowStatus.SOLD_OUT)
    movie3.book_tickets(customer1,2)
except Exception as e:
    print(f'{e} - {type(e).__name__}')

#Booking a Cancelled Show
try:
    movie4=MovieShow('Sky',30,1,ShowStatus.OPEN)
    movie4.cancel_show()
    movie4.book_tickets(customer1,2)
except Exception as e:
    print(f'{e} - {type(e).__name__}')

#invalid capacity
try:
    movie5=MovieShow('Minions 2',0,2,ShowStatus.OPEN)
  
except Exception as e:
    print(f'{e} - {type(e).__name__}')

#invalid status
try:
    movie5=MovieShow('Minions 2',10,2,'Open')
  
except Exception as e:
    print(f'{e} - {type(e).__name__}')