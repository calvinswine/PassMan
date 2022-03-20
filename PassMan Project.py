print("Welcome to PassMan 1.0: The One Stop Destination for all your passwords")

user_id = input("Enter your user id for the password manager: ")
password_entered = input("Enter your password for the password manager: ")

user_id_list = list()
password = "calisthenicmovement.69"

if user_id in user_id_list:
    if password_entered == password:
        print("Welcome back", user_id)
        choice = input("Make a choice for either seeing all of your existing passwords or to enter new passwords(see/new): ")
        if choice == "new":
            #write code for entering new passwords
        elif choice == "see":
            #write code for seeing existing passwords
            #also make a loop if a person enters a wrong choice, then he gets more chances to enter the right choices
    else:
        print("Your password is incorrect")
else:
    print("Your username is not registered in the database.")
    #also make a loop if a person enters a wrong choice, then he gets more chances to enter the right choices