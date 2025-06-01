Name = input("what is your Name? ")
Age = int(input("How old are you?"))
Gpa = float(input("what is your GPA?(1.0 -5.0)"))
Interest = input("what is your field of interest?")
Grad = input("did you graduate?(yes/no)").lower()


if Age < 25 and Gpa >= 3.5 and Grad == "yes":
    print(Name.capitalize(),", you are eligible for a scholarship")

elif Age < 30 and Gpa >= 2.5:
    print(Name.capitalize(),", you are eligible for an internship")     
else:
    print("we recommend you apply later")