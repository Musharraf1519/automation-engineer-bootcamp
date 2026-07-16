print("=========================================================================")
print("                    STUDENT INFORMATION SYSTEM")
print("=========================================================================")

student_id = input("Enter Student ID        : ")
name = input("Enter Name              : ")
age = int(input("Enter Age               : "))
gender = input("Enter Gender            : ")
dob = input("Enter Date of Birth     : ")
print()
course = input("Enter Course            : ")
branch = input("Enter Branch            : ")
semester = int(input("Enter Semester          : "))
college = input("Enter College           : ")
print()
email = input("Enter Email             : ")
mobile = input("Enter Mobile Number     : ")
city = input("Enter City              : ")
state = input("Enter State             : ")
country = input("Enter Country           : ")
print()
marks_1 = int(input("Enter Subject 1 Marks   : "))
marks_2 = int(input("Enter Subject 2 Marks   : "))
marks_3 = int(input("Enter Subject 3 Marks   : "))
marks_4 = int(input("Enter Subject 4 Marks   : "))
marks_5 = int(input("Enter Subject 5 Marks   : "))

print("=========================================================================")
print("                        STUDENT REPORT")
print("=========================================================================")

print("PERSONAL INFORMATION")
print("------------------------------------------------------------")

print(f"Student ID        : {student_id}")
print(f"Name              : {name}")
print(f"Age               : {age}")
print(f"Gender            : {gender}")
print(f"Date of Birth     : {dob}")

print("ACADEMIC INFORMATION")
print("------------------------------------------------------------")

print(f"Course            : {course}")
print(f"Branch            : {branch}")
print(f"Semester          : {semester}")
print(f"College           : {college}")

print("CONTACT INFORMATION")
print("------------------------------------------------------------")

print(f"Email             : {email}")
print(f"Mobile            : {mobile}")
print(f"City              : {city}")
print(f"State             : {state}")
print(f"Country           : {country}")

print("MARKS")
print("------------------------------------------------------------")

print(f"Subject 1         : {marks_1}")
print(f"Subject 2         : {marks_2}")
print(f"Subject 3         : {marks_3}")
print(f"Subject 4         : {marks_4}")
print(f"Subject 5         : {marks_5}")

print("RESULT")
print("------------------------------------------------------------")

total = marks_1+marks_2+marks_3+marks_4+marks_5

print(f"Total Marks       : {total}")
print(f"Average Marks     : {total/5}")
print(f"Percentage        : {total/5}%")

print("=========================================================================")