from status import CourseStatus
from course import Course
from mode import DeliveryMode

##Importing student_level enum and Student class
from student_expertise import StudentLevels
from student import Student



##TESTING IN MAIN ENUMS AND METHODS ADDED

course1=Course("Advanced Programming", 10 , CourseStatus.OPEN, DeliveryMode.IN_PERSON)
course2=Course("Web Interface Programming", 50, CourseStatus.CLOSED,DeliveryMode.ONLINE)

course1.display_info()
course2.display_info()


##Closing registration for course1
course1.close_registration()
course1.display_info()


##Reopening registrationn for  course2
course2.reopen_course()
course2.display_info()

print ("-----------------------")

#CREATIG STUDENT

student1=Student("Karla","Flores",StudentLevels.ADVANCED)
student1.display_info()