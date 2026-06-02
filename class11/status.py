from enum import Enum

class CourseStatus(Enum):
    OPEN= "open"
    CLOSED="closed"
    CANCELLED= "cancelled"

##status=CourseStatus.CLOSED 
##print(status)##It will print "CourseStatus.CLOSED"

#print(CourseStatus.OPEN.value) ##It will print the actual value inside
