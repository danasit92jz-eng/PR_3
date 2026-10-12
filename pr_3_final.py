#Project: Student Data Organizer
#For student record
stu = []
#Set fro unique subject
all_sub = set()
print("==========Welcome to Student Data Organizer.==========")
while True:
    print("\n*********MAIN MENU*********")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            sid = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter DOB: ")

            # Check ID already exists
            if any(s["id"] == sid for s in stu):
                print("Student ID already exists!")
            else:
                sub = input("Enter Subjects as comma-separated input: ")
                # Convert string into a list
                subjects = [x.strip() for x in sub.split(",")]
                # Store ID and DOB in a tuple
                identity = (sid, dob)
                # Store student details in a dictionary
                student = {"identity": identity,"id": sid,"name": name,"age": age,"grade": grade,"subjects": subjects}
                # Add dictionary to the main list
                stu.append(student)
                # Add subjects to set (duplicates removed)
                all_sub.update(subjects)
                print("Student added successfully!")
        case 2:
            if len(stu) == 0:
                print("No student records found.")
            else:
                print("\n----- ALL STUDENTS -----")
                for s in stu:
                    print(f"ID:{s['id']} | Name:{s['name']} | Age:{s['age']} | Grade:{s['grade']}")
                    print("Subjects: {}".format(", ".join(s["subjects"])))
                    print("DOB:", s["identity"][1])
                    print("\n__________________")
        case 3:
            sid = int(input("Enter Student ID for update_record: "))
            for s in stu:
                if s["id"] == sid:
                    print("1. Update Age")
                    print("2. Update Grade")
                    print("3. Update Subjects")
                    ch = int(input("Enter your choice: "))
                    match ch:
                        case 1:
                            # Update age
                            s["age"] = int(input("Enter new age: "))
                            print("Age updated successfully!")
                        case 2:
                            # Update grade
                            s["grade"] = input("Enter new grade: ")
                            print("Grade updated successfully!")
                        case 3:
                            # Update subjects
                            sub = input("Enter new subjects: ")
                            s["subjects"] = [x.strip() for x in sub.split(",")]
                            print("Subjects updated successfully!")
                        case _:
                            print("Invalid choice!")
                    print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
                    print("Subjects: {}".format(",".join(s["subjects"])))
                    
                    # Recalculate unique subjects
                    all_sub.clear()
                    for st in stu:
                        all_sub.update(st["subjects"])
                    break

            else:
                print("Student ID not found!")
        case 4:
            sid = int(input("Enter Student ID for delete record: "))
            for i in range(len(stu)):
                if stu[i]["id"] == sid:
                    del stu[i]
                    print("record deleted successfully!")
                    all_sub.clear()
                    for s in stu:
                        all_sub.update(s["subjects"])
                    break
            else:
                print("Student ID not found!")
        case 5:
            print("\n----- SUBJECTS OFFERED -----")
            if len(all_sub) == 0:
                print("No subjects available.")
            else:
                for s in sorted(all_sub):
                    print(s)
        case 6:
            print("Thank you for using Student Data Organizer!")
            break
        case _:
            print("Invalid choice! Please enter 1 to 6.")

            
            



