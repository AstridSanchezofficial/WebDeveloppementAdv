class courseSection:
    def __init__(self,title,capacity,enrolled):
        self.title=title
        self.capacity=capacity
        self.enrolled=enrolled
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity (self,amount):
        if amount <=0:
            raise ValueError('Add a real capacity')
        self.__capacity=amount
        print(f"The current capacity for the {self.title} course is {self.capacity} spots")

    @property
    def enrolled(self):
            return self.__enrolled
    
    @enrolled.setter
    def enrolled(self,studentsEnrolled):
        if 0 <= studentsEnrolled <= self.__capacity:
           self.__enrolled=studentsEnrolled
           print(f"{self.__enrolled} spots were reserved for {self.title} course")
        else:
            raise ValueError(
            f"We cannot reserve {studentsEnrolled} spots. "
            f"Current available spots: {self.__capacity}"
            )
        
    ##Adding methods

    def register_student(self):
        self.enrolled+=1

    def drop_student(self):
        self.enrolled-=1
        print(f"One student just dropped the course")

    def display_info(self):
       print(f"{self.title} has {self.__enrolled} students enrolled / {self.capacity} spots available") 

    


