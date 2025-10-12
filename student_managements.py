import pandas as pd  
from collections import Counter  
import datetime  
  
students = {}  
print("---------- Welcome to Student Result Management System ----------")  
  
while True:  
    print("\n--- MENU ---")  
    print("1. Add Student")  
    print("2. View Student Data")  
    print("3. Update Marks")  
    print("4. Update Phone Number")  
    print("5. Delete Student")  
    print("6. Display All Students")  
    print("7. Save Data to CSV")  
    print("8. View Summary Stats")  
    print("9. Exit")  
  
    choice = input("\nEnter your choice (1-9): ")  
  
    if choice == "1":  
        roll = input("Enter Roll Number: ")  
        if roll in students:  
            print("Student already exists.")  
        else:  
            name = input("Enter Name: ")  
            student_class = input("Enter Class: ")  
            phone = input("Enter Phone Number: ")  
            school = input("Enter School Name: ")  
  
            try:  
                m1 = float(input("Enter Marks for Subject 1: "))  
                m2 = float(input("Enter Marks for Subject 2: "))  
                m3 = float(input("Enter Marks for Subject 3: "))  
                if not all(0 <= mark <= 100 for mark in [m1, m2, m3]):  
                    raise ValueError  
            except ValueError:  
                print("Invalid marks input. Setting all to 0.")  
                m1 = m2 = m3 = 0.0  
  
            total = m1 + m2 + m3  
            percentage = round((total / 300) * 100, 2)  
  
            if percentage >= 90:  
                grade = "A+"  
            elif percentage >= 80:  
                grade = "A"  
            elif percentage >= 70:  
                grade = "B"  
            elif percentage >= 60:  
                grade = "C"  
            elif percentage >= 50:  
                grade = "D"  
            else:  
                grade = "F"  
  
            students[roll] = {  
                "Name": name,  
                "Class": student_class,  
                "Phone": phone,  
                "School": school,  
                "Marks": [m1, m2, m3],  
                "Total": total,  
                "Percentage": percentage,  
                "Grade": grade  
            }  
            print("Student added successfully.")  
  
    elif choice == "2":  
        roll = input("Enter Roll Number: ")  
        if roll in students:  
            print("\n--- Student Data ---")  
            for key, val in students[roll].items():  
                print(f"{key}: {val}")  
        else:  
            print("Student not found.")  
  
    elif choice == "3":  
        roll = input("Enter Roll Number: ")  
        if roll in students:  
            try:  
                m1 = float(input("Enter new Marks for Subject 1: "))  
                m2 = float(input("Enter new Marks for Subject 2: "))  
                m3 = float(input("Enter new Marks for Subject 3: "))  
                if not all(0 <= mark <= 100 for mark in [m1, m2, m3]):  
                    raise ValueError  
            except ValueError:  
                print("Invalid input.")  
                continue  
  
            total = m1 + m2 + m3  
            percentage = round((total / 300) * 100, 2)  
  
            if percentage >= 90:  
                grade = "A+"  
            elif percentage >= 80:  
                grade = "A"  
            elif percentage >= 70:  
                grade = "B"  
            elif percentage >= 60:  
                grade = "C"  
            elif percentage >= 50:  
                grade = "D"  
            else:  
                grade = "F"  
  
            students[roll]["Marks"] = [m1, m2, m3]  
            students[roll]["Total"] = total  
            students[roll]["Percentage"] = percentage  
            students[roll]["Grade"] = grade  
            print("Marks updated successfully.")  
        else:  
            print("Student not found.")  
  
    elif choice == "4":  
        roll = input("Enter Roll Number: ")  
        if roll in students:  
            new_phone = input("Enter new Phone Number: ")  
            if new_phone.isdigit():  
                students[roll]["Phone"] = new_phone  
                print("Phone updated successfully.")  
            else:  
                print("Invalid phone number.")  
        else:  
            print("Student not found.")  
  
    elif choice == "5":  
        roll = input("Enter Roll Number to Delete: ")  
        if roll in students:  
            del students[roll]  
            print("Student deleted successfully.")  
        else:  
            print("Student not found.")  
  
    elif choice == "6":  
        if students:  
            print("\n--- All Student Records ---")  
            for roll, details in students.items():  
                print(f"\nRoll No: {roll}")  
                for key, val in details.items():  
                    print(f"  {key}: {val}")  
        else:  
            print("No records found.")  
  
    elif choice == "7":  
        if students:  
            df = pd.DataFrame.from_dict(students, orient='index')  
            filename = f"student_records_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"  
            df.to_csv(filename)  
            print(f"Data saved to '{filename}' successfully.")  
        else:  
            print("No data to save.")  
  
    elif choice == "8":  
        if students:  
            percentages = [data["Percentage"] for data in students.values()]  
            grades = [data["Grade"] for data in students.values()]  
            avg = round(sum(percentages) / len(percentages), 2)  
            grade_count = Counter(grades)  
            print(f"\nAverage Percentage: {avg}%")  
            print("Grade Distribution:")  
            for grade, count in grade_count.items():  
                print(f"  {grade}: {count}")  
        else:  
            print("No data to analyze.")  
  
    elif choice == "9":  
        print("Exiting program. Goodbye.")  
        break  
  
    else:  
        print("Invalid choice. Please enter a number between 1 and 9.")  
  
    cont = input("\nDo you want to continue? (y/n): ").lower()  
    if cont != 'y':  
        print("Exiting program. Goodbye.")  
        break