from status import CourseStatus
from mode import DeliveryMode

class Course:

    MAX_CAPACITY=60
    def __init__(self,title,capacity,status,delivery_mode):
        self.title=title
        self.capacity=capacity
        self.status=status
        self.course_version=delivery_mode

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,value):
        if not isinstance(value ,CourseStatus):
            raise ValueError ("status must be a CourseStatus value")
        
        self.__status=value

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,value):
        
        if 0 < value <= self.MAX_CAPACITY:
            self._capacity=value
        else:
            raise ValueError (f"Capacity must be between 0 and {self.MAX_CAPACITY}")

    #Validating mode check _ and public with teacher 

    @property
    def course_version(self):
        return self._course_version

    @course_version.setter
    def course_version (self, delivery_mode):
        if not isinstance(delivery_mode , DeliveryMode):
            raise ValueError ("course mode must be in DeliveryMode ")
        self._course_version=delivery_mode


    def display_info(self):
        print(f"Course title:{self.title} | Capacity:{self.capacity} | Status: {self.status.value} | Mode : {self.course_version.value}")

    def close_registration(self):
        self.status=CourseStatus.CLOSED

    def cancel_Course(self):
        self.status=CourseStatus.CANCELLED

    def reopen_course(self):
        self.status=CourseStatus.OPEN

  ##TESTING  
#course1=Course("Math",45,CourseStatus.OPEN)
#course1.display_info()
