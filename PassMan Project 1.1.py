print("Welcome to PassMan 1.0: The One Stop Destination for all your passwords")
print("")

data = dict()

user_id = input("Enter your user id for the password manager: ")
password_entered = input("Enter your password for the password manager: ")
print("")

user_id_list = ["calvinswine"]
password = "calisthenicmovement.69"

error = True
choice2 = None

if user_id in user_id_list:
    
    if password_entered == password:
        print("Welcome back", user_id)
        choice = input("Choose whether you want to enter new credentials or view all your existing ones or view a specific one: (new/view/one): ")
        print("")


        while((error == True) or (choice2 == 'y')):
            
            if choice == "new":
                website = input("Enter the name of the website for which you want to store the credentials: ")
                username = input("Enter your username on the website: ")
                password = input("Enter your password for the website: ")
                print("")

                data[website] = {username : password}
                error = False
                print("")

                print("Your credentials have been added to our database (for you) successfully!")
                print(data)
                print("")
                
                choice2 = input("Would you like to enter another credential? (y/n): ")
                print("")

            elif choice == "view":
                print("Here you go!")
                print(data)
                error = False
            elif choice == "one":
                website = input("Enter the name for the website for which you want to view your saved credentials: ")
                print(data[website])
            else:
                print("ERROR!")
                print("") 

                error = True
                choice = input("Choose whether you want to enter new credentials or view all your existing ones or view a specific one: (new/view/one): ")
                print("")
        
        if choice2 == 'n':
            print("Alrighty then, Have a great day!")
    
    else:
        print("Your password is incorrect.")

else:
    print("Your username is not registered.")
    print("")

    sign_up = input("Would you like to register with us in our database? (y/n) (Wrong choice in the input box below will abort the process.): ")
    print("")

    
    if sign_up == "y":
        user_id = input("Enter your user id for the PassMan app: ")
        password = input("Enter your password for the PassMan app: ")
        user_id_list.append(user_id)
        print("")
        
        print("Successfully registered!")
        print("")

        print("Note: If you forget the password to your PassMan application, then there is no way of recovering this password. So, we suggest you to write down this password somewhere and keep it safe. If this falls into the hands of any person, then he can use this password for viewing all of your saved passwords. So, be careful about where you keep this. We will be introducing two-step verification the future, but until then, it is what it is.")
    elif sign_up == "n":
        print("Alrighty then, Have a great day!")
    else:
        print("Aborting...")
        print("Aborted successfully!")