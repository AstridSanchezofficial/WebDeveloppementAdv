from status import ShowStatus
from user import User,Customer,Staff
from exceptions import InvalidBookingError,InvalidStatusError,ShowSoldOutError,ShowCancelledError
# Part 4 - Main Businnes Class

class MovieShow():
    MAX_TICKETS_PER_BOOKING=5
    def __init__(self,title,capacity,booked_seats,status):
        self.title=title
        self.capacity=capacity
        self.booked_seats=booked_seats
        self.status=status

    @property
    def title(self):
        return self.__title
    
    # Title cannot be empty 
    @title.setter
    def title(self,movie_name):
        if not isinstance(movie_name,str) or movie_name.strip()=="":
            raise ValueError ('PLease enter a valid movie name')
        else:
            self.__title=movie_name
          
        
   
    @property
    def capacity(self):
        return self.__capacity
    
     # Capacity must be greater than 0
    @capacity.setter
    def capacity(self,value):
        if not isinstance(value,int) or value <= 0:
            raise ValueError('Enter a valid number capacity , greater than 0')

        else:
            self.__capacity=value
           

    @property 
    def booked_seats(self):
        return self.__booked_seats
    
    @booked_seats.setter
    def booked_seats(self,value):
        if not isinstance(value,int) or value < 0 or value > self.capacity:
            raise ValueError(f'Make sure you booked between 0 and {self.capacity} seats')
        else:
            self.__booked_seats=value
    @property
    def status(self):
        return self.__status
    
    # Using Enum 
    @status.setter
    def status (self,movie_status):
        if not isinstance(movie_status,ShowStatus):
            raise InvalidStatusError ('Enter a valid movie status')
        else:
            self.__status=movie_status
    @property
    def remaining_seats(self):
        remainining=self.capacity-self.booked_seats
        return remainining

    ##METHODS
    def book_tickets(self,customer,quantity):
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if quantity > MovieShow.MAX_TICKETS_PER_BOOKING:
            raise InvalidBookingError(f"Max {MovieShow.MAX_TICKETS_PER_BOOKING} tickets per booking")

        if self.status == ShowStatus.CANCELLED:
            raise ShowCancelledError("Cannot book tickets: show cancelled")
        
        if self.status == ShowStatus.SOLD_OUT:
            raise ShowSoldOutError("Cannot book tickets: It is sold out")

        if quantity > self.remaining_seats:
            raise InvalidBookingError(f"Only {self.remaining_seats} seats remaining")

        # booking
        self.booked_seats += quantity

        # update status if full
        if self.remaining_seats == 0:
            self.status = ShowStatus.SOLD_OUT
            

        print (f"{quantity} tickets booked for {customer.name}")

    def cancel_show(self):
        self.status=ShowStatus.CANCELLED
    def display_info(self):
        print(f'Title: {self.title} | capacity: {self.capacity} | Booked seats: {self.booked_seats} | Status: {self.status.value}')
    
# movie1=MovieShow("Scary movie",9,2,ShowStatus.OPEN)
# movie1.display_info()
# print(movie1.remaining_seats)
# print(movie1.remaining_seats())
# movie1=MovieShow("White girls",34,30,ShowStatus.OPEN)
# customer1=Customer("Carol","carol@yahoo.com",3) 
# movie1.display_info()

# movie1.book_tickets(customer1,4)
# movie1.display_info()



        


    