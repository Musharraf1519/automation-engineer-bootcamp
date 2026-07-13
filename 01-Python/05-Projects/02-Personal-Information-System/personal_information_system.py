name = "Musharraf Hussain Khan"
age = 30
gender = "Male"
is_married = False
city = "Bengaluru"
country = "India"
email = "musharrafhussainkhan@gmail.com"
phone_no = "9875720074"
emergency_contact = "9038720074"
monthly_salary = 100211
occupation = "I.T. Engineer"
manager = None
passport_no = "T28348"
height_cm  = 167.64
weight_kg = 74.64
blood_group = "AB+"
annual_income = monthly_salary*12
age_after_10_years = age+10
height_mtrs = height_cm/100
bmi = (weight_kg/(height_cm*height_cm))*10000



print("==============================================================")
print("                 PERSONAL INFORMATION SYSTEM")
print("==============================================================")

print("\nPersonal Details")
print("--------------------------------------------------------------")
print(f"Name                : {name}")
print(f"Age                 : {age}")
print(f"Gender              : {gender}")
print(f"Is Married          : {is_married}")
print(f"Age after 10 years  : {age_after_10_years}")
print("--------------------------------------------------------------")

print("\nContact Details")
print("--------------------------------------------------------------")
print(f"City                : {city}")
print(f"Country             : {country}")
print(f"Email               : {email}")
print(f"Phone               : {phone_no}")
print(f"Emergency Contact   : {emergency_contact}")
print("--------------------------------------------------------------")

print("\nFinancial Details")
print("--------------------------------------------------------------")
print(f"Monthly Income      : ₹{monthly_salary}")
print(f"Annual Income       : ₹{annual_income}")
print("--------------------------------------------------------------")

print("\nProfessional Details")
print("--------------------------------------------------------------")
print(f"Occupation          : {occupation}")
print(f"Manager             : {manager}")
print("--------------------------------------------------------------")

print("\nIdentification Details")
print("--------------------------------------------------------------")
print(f"Passport No         : {passport_no}")
print("--------------------------------------------------------------")

print(f"\nHealth Details")
print("--------------------------------------------------------------")
print(f"Height              : {height_cm} cm")
print(f"Height in Meters    : {height_mtrs} cm")
print(f"Weight              : {weight_kg} kg")
print(f"Blood Group         : {blood_group}")
print(f"BMI                 : {bmi}")
print("--------------------------------------------------------------")

print("\nDatatype Summary")
print("--------------------------------------------------------------")
print(f"Name                : {type(name)}")
print(f"Age                 : {type(age)}")
print(f"Height              : {type(height_cm)}")
print(f"Weight              : {type(weight_kg)}")
print(f"Gender              : {type(gender)}")
print(f"Monthly Income      : float")
print(f"Is Married          : bool")
print(f"Manager             : NoneType")
print(f"City                : {type(city)}")
print(f"Country             : {type(country)}")
print(f"Email               : {type(email)}")
print(f"Phone Number        : {type(phone_no)}")
print(f"Occupation          : {type(occupation)}")
print(f"Blood Group         : {type(blood_group)}")
print(f"Passport Number     : {type(passport_no)}")
print(f"Emergency Contact   : {type(emergency_contact)}")
print("==============================================================")