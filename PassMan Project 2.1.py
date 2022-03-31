print("")
print("Welcome to PassMan 2.1: The One Stop Destination for all your passwords")
print("")


file = open("Data.txt", 'a')

data = dict()

user_id = input("Enter your user id for PassMan application: ")
password_entered = input("Enter your password for the same: ")

# file.write("User I.D. = " + user_id + "\n")
# file.write("Password = " + password_entered + "\n")

index = 0
flag = 0

file2 = open("Data.txt", 'r')

for i in file2:
    if user_id in i:
        flag = 1
        line = index
        break
    index+=1

contents = file2.readlines()

error = True #error variable is created so that if the user makes an error in writing the input for choice variable, he can get the chance to input the variable again
choice2 = None #choice2 variable is created so that if the user wants to enter more credentials, then he can get the chance to do so


if flag == 1:
    
    if password_entered in contents[line]:
        print("Welcome back", user_id)
        choice = input("Choose whether you want to enter new credentials or view all your existing ones or view a specific one: (new/view/one): ")
        print("")

        while((error == True) or (choice2 == 'y')):

            if choice == "new":
                website = input("Enter the name of the website for which you want to store credentials: ")
                username = input("Enter your username on the website: ")
                password =  input("Enter your password for the website: ")
                print("")

                data[website] = {username : password}
                file.write("data = " + str(data) + "\n")
                error = False
                print("")

                print("Your credentials have been added to our database successfully!")
                print("")

                choice2 = input("Would you like to enter another credential? (y/n): ")
                print("")

            elif choice == "view":
                file3 = open("Data.txt", 'r')
                
                for i in file3:
                    if "data" in i: ##there is one problem here though. If this data belongs to someone else, which it likely will if there are multiple users in the PassMan, then the data for some other user will get printed. So, you need to make changes to the code in such a way that the username of the user needs to be written alongside the word data and then iterate with that username along with the word data.
                        print(i)
                        break
                
                file3.close()

            elif choice == "one":
                website = input("Enter the name for the website for which you want to view your saved credentials:")
                file3 = open("Data.txt", 'r')

                for i in file3:
                    if website in i: ##there is a problem here. If someone else has also saved credentials for the same website in their database, then it will not work properly. Fix this.
                        string = i
                        break
                
                file3.close()

                string_new = string[string.index('{') : ] #here, the string which was defined earlier is getting sliced so that only the dictionary part of the entire string remains
                
                import json

                dict1 = json.loads(string_new)

                print("Here are your credentials for", website)
                print(dict1[website])

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

    if sign_up == 'y':
        user_id = input("Enter your user id for the PassMan app: ")
        password = input("Enter your password for the same: ")
        print("")
        
        file.write("User I.D. = " + user_id + "\n")
        file.write("Password = " + password_entered + "\n")

        print("Successfully registered!")
        print("")

        print("Note: If you forget the password to your PassMan application, then there is no way of recovering this password. So, we suggest you to write down this password somewhere and keep it safe. If this falls into the hands of any person, then he can use this password for viewing all of your saved passwords. So, be careful about where you keep this. We will be introducing two-step verification the future, but until then, it is what it is.")
        print("")

    elif sign_up == 'n':
        print("Alrighty then, have a great day!")
    else:
        print("Aborting...")
        print("Aborted successfully!")