from student_expertise import StudentLevels

class Student():
    def __init__(self,name,last_name,student_level):
        self.name=name
        self.last_name=last_name
        self.expertise=student_level

    @property 
    def expertise(self):
        return self._expertise
    
    @expertise.setter
    def  expertise(self,student_level):
        if not isinstance (student_level,StudentLevels):
            raise ValueError ("student level must be a StudentLevels value")
        self._expertise=student_level

    def display_info(self):
        print(f"Name:{self.name}, Lastname:{self.last_name} | Type of student:{self.expertise.value}")


