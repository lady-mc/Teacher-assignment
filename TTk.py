import getpass
from datetime import datetime
import re

# """so this is the beginning of a learning website"""

# # --step 1: welcome message. 

message = "Welcome to TTK"
print(message)

# --step 2:  registration --
# ask parents for bio data

parent = {}

parent['Name'] = input("Enter Parent/Guardian Full Name:")

#--phone validation: must be 10-11 digits 
while True:
    phone = input("Enter Phone Number.(WhatsApp preferred):")
    if re.fullmatch(r"\d{10,11}", phone):
        parent['phone'] = phone
        break
    else:
        print("Invalid phone number. Use 10-11 digits only.")

# --Email validation--

while True:
    email = input("Enter Email address:")
    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        parent['email'] = email
        break
    else: 
        print("invalid email format. Example: anna@mail.com")

parent['Home_Address'] = input("Home Address (optional):")
parent['Relationship_to_Child'] = input("Enter Relationship_to_Child: ")

#-- choice of communication --
print("Preferred Method of Communication")

methods = {
    "1": "WhatsApp",
    "2": "Phone call",
    "3": "Email"
}

print("\n--- Preferred Method of Communication ---")
for key, value in methods.items():
    print(f"{key} - {value}")

while True:
    choice = input("Enter the number of your choice: ")

    if choice in methods:
        parent['communication'] = methods[choice]
        break
    else:
        print("Invalid selection. Please try again.")

#--password creation--

while True:
    password = getpass.getpass("Create a password (min 6 chars, must include a number): ")
    confirm = getpass.getpass("Confirm password: ")

    if password != confirm:
        print("Passwords do not match. Try again.")
    elif len(password) < 6:
        print("Password must be at least 6 characters long.")
    elif not any(char.isdigit() for char in password):
        print("password must include at least one number.")
    else:
        parent['password'] = password
        print("password created successfully.\n")
        break
    

#--CHILD / STUDENT INFORMATION --

#--(Linked to parent’s account)--

#--choice for multiple kids--
parent['children'] = []

while True:
    
    child = {}
    
    #child info
    child['Name'] = input("Enter Child's Full Name:")
    child['Gender'] = input("Enter Child's Gender:")

#-- date of birth validation --

    while True:
        dob_input = input("Enter Child's Date of Birth (DD/MM/YYYY): ")
        try:
            dob = datetime.strptime(dob_input, "%d/%m/%Y")
            child['dob'] = dob_input
            break
        except ValueError:
            print("Invalid format. Please use DD/MM/YYYY.")

    child['Grade'] = input("Enter Child's Grade/class:")

#--course selection--
#--Available courses--
    Available_courses = ["Scratch", "python", "c++", "CSS", "HTML"]

    print("\n Available Courses")
    for i, courses in enumerate(Available_courses, 1):
        print(f"{i}. {courses}")
        
    while True:
        choices = input("Enter the numbers of courses to enroll (comma separated, e.g., 1,3,5): ")
        try:
            selected_courses = [Available_courses[int(i)-1] for i in choices.split(",")]
            child['courses'] = selected_courses
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers from the list, separated by commas.")

    print("\n Courses selected:", child['courses'])

#-- Previous Knowledge (Beginner / Intermediate / Advanced)

    knowledge_levels = {
        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced"
    }

    print("\nPrevious Knowledge Level:")
    for key, value in knowledge_levels.items():
        print(f"{key} - {value}")

    while True:
        choice = input("Select knowledge level (1-3): ")
        if choice in knowledge_levels:
            child['previous_knowledge'] = knowledge_levels[choice]
            break
        else:
            print("Invalid choice. Please try again.")


#-- Special Learning Needs (optional)--

    special_needs = input("\n Any special learning needs? (Press Enter if none): ")
    
    if special_needs.strip() == "":
        child['special_learning_needs'] = "None"
    else:
        child['special_learning_needs'] = special_needs

#-- add child to parent list --
    parent['children'].append(child)
    
#--ask if another child--
    another = input("\nDo you want to add another child? (yes/no): ").lower()
    if another == "no":
        break

    print("\n--- Registration Complete! ---")
print(f"Parent: {parent['Name']} - {parent['phone']} - {parent['email']} - {parent['communication']}")
print(f"Number of children registered: {len(parent['children'])}\n")

for idx, c in enumerate(parent['children'], 1):
    print(f"Child {idx}: {c['Name']}, DOB: {c['dob']}, Grade: {c['Grade']}")
    print(f"Courses: {c['courses']}")
    print(f"Previous Knowledge: {c['previous_knowledge']}")
    print(f"Special Needs: {c['special_learning_needs']}\n")
