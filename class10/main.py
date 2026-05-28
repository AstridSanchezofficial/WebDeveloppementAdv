from student_record import studentRecord
from course_section import courseSection

if __name__ == "__main__":

    # NORMAL
    course1 = courseSection("Prototyping II", 40, 1)
    course1.register_student()
    course1.display_info()

    # ERROR TEST
    try:
        course2 = courseSection("Math", 10, 50)
    except ValueError as e:
        print("Caught error:", e)

    # LIMIT TEST
    course3 = courseSection("Physics", 2, 2)
    try:
        course3.register_student()
        course3.display_info()
    except ValueError as e:
        print("Limit reached:", e)

    #Trying to remove more students than currently enrolled
    
    course4=courseSection("Data Visualisation",40,1)
    try:
        course4.drop_student()
        course4.drop_student()
        course4.display_info()
    except ValueError as e:
        print("You are substracting more students than expected:",e)


    print("---------")


    #NORMAL

    student1=studentRecord("Danielle Daria",4.0,36)
    student1.add_credits(20)
    student1.update_gpa(3.5)


    #ADDING NEGATIVE CREDITS

    student2=studentRecord("Oumaima",3.9,24)
    try:
        student2.add_credits(-34)
    except ValueError as e:
        print("You are entering a negative value!:",e)

    #INVALID GPA

  
    try:
        student3=studentRecord("Laura",5.0,12)
    except ValueError as e:
        print("Invalid Gpa!",e)

    #UPDATING AN INVALID GPA
    student4=studentRecord("Gmaima",2.9,24)
    try:
        student4.update_gpa(-3.9)
    except ValueError as e:
        print("Imposible to update the GPA.",e)

   ## Testing academic_status only-read property
    print(student4.academic_status)#TWe are able just to read not modify the output
   