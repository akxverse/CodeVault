students={}
def add_student():
    rollnumber = int(input("Enter the roll number: "))
    if rollnumber in students:
        print("Student already exists")
        return
    name=input("Enter the name: ")
    branch=input("Enter the branch: ")
    admissionyear = int(input("Enter the admission year: "))
    while True:
        phone = input("Enter the phone number: ")
        if len(phone)!=10 or not phone.isdigit():
                print("invalid phone number!!! please enter again")
        else:
            break

    while True:
        email = input("Enter the email: ")
        if "@" not in email or ".com" not in email:
            print("Invalid email please try again")
        else:
            break


    semester=input("Enter the semester: ")

    while True:
        try:
            cgpa = float(input("Enter the cgpa (0-10): "))
            if 0 <= cgpa <= 10:
                break
            else:
                print("CGPA must be between 0 and 10")
        except:
            print("Please enter numbers only!")


    year=int(input("Enter the year: "))
    students[rollnumber]={"Name":name,"Branch":branch,"Admission_year":admissionyear,"Contact":(phone,email),"Academic_History":(semester,cgpa,year)}

def fetch_student():
    roll=input("Enter the roll number: ")
    if roll in students:
            print(students[roll])
    else:
        print("Roll number not found")

def update_student():
    rollnumber=input("Enter the roll number to update: ")
    if rollnumber in students:
        field=input("Enter the field to update: ")
        match field:
            case "name":
                students[rollnumber]["Name"]=input("Update the name: ")
                print("Name updated")
            case "branch":
                students[rollnumber]["Branch"]=input("Update the branch: ")
                print("Branch updated")
            case "admission_year":
                students[rollnumber]["Admission_year"]=input("Update the admission year: ")
                print("Admission year updated")
            case "contact":
                while True:
                    phone = input("update the phone number: ")
                    if len(phone)!=10 or not phone.isdigit():
                        print("invalid phone number!!! please enter again")
                    else:
                        break
                while True:
                    email = input("update the email: ")
                    if "@" not in email or ".com" not in email:
                        print("Invalid email please try again")
                    else:
                        break
                students[rollnumber]["Contact"]=(phone,email)
                print("Contact updated")

            case "academic_history":
                semester=input("Enter the semester: ")

                while True:
                    try:
                        cgpa = float(input("Enter the updated cgpa (0-10): "))
                        if 0 <= cgpa <= 10:
                            break
                        else:
                            print("CGPA must be between 0 and 10")
                    except:
                        print("Please enter numbers only!")

                year=int(input("Enter the year: "))
                students[rollnumber]["Academic_History"]=(semester,cgpa,year)
                print("Academic History Updated successfully")

            case _:
                print("Invalid input")

def display_all():
    for key, val in students.items():
        print(f"{key} | {val["Name"]} | { val["Branch"]} | {val["Admission_year"]} | {val["Contact"]} | {val["Academic_History"][2]}")
display_all()

def find_by_branch():
    branch = input("Enter the branch: ")
    for key,val in students.items():
        if branch==val["Branch"]:
                 print(val["Name"])

def compare_cgpa():
    roll1=input("Enter the roll number: ")
    roll2=input("Enter the roll number: ")
    if roll1 and roll2 in students:
        print(f"Cgpa of {roll1}",students[roll1]["Academic_History"][1])
        print(f"Cgpa of {roll2}",  students[roll2]["Academic_History"][1])
        if students[roll1]["Academic_History"][1]>students[roll2]["Academic_History"][1]:
            print(f"cgpa of {roll1} is greater than cgpa of {roll2}")
        elif students[roll1]["Academic_History"][1]==students[roll2]["Academic_History"][1]:
            print("both are equal")

        else:
            print(f"cgpa of {roll2} is greater than cgpa of {roll1}")
    else:
        print("Roll number not found")




while True:
    print("enter 1 to add student record")
    print("enter 2 to fetch student record")
    print("enter 3 to update student record")
    print("enter 4 to display all student record")
    print("enter 5 to find by branch:")
    print("enter 6 to compare academic performance")
    print("enter e key to exit")
    choice=input("Enter your choice:")
    if choice=="e":
        break
    try:
        choice=int(choice)
    except Exception as e:
        print("Please enter a valid choice!!!")
        continue
    match choice:
        case 1:add_student()
        case 2: fetch_student()
        case 3: update_student()
        case 4: display_all()
        case 5: find_by_branch()
        case 6: compare_cgpa()










