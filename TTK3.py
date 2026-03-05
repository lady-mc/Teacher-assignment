parents = [] #will store all parent accounts

#function that allows parent to sign up

def parent_signup():

    name = input("Enter parent name: ")
    email = input("Enter parent email: ")

    parent = {
        "name": name,
        "email": email,
        "children": []
    }

    parents.append(parent)

    print("Parent registered successfully")


parent_signup()

print(parents)