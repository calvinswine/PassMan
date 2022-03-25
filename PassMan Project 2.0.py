print("Welcome to PassMan 2.0: The One Stop Destination for all your passwords")
print("")


file = open("Data.txt", 'a')

data = dict()

user_id = input("Enter your user id for PassMan application: ")
password_entered = input("Enter your password for the same: ")

file.write("User I.D. = " + user_id + "\n")
file.write("Password = " + password_entered + "\n")

index = 0
flag = 0

for i in file:
    if user_id in i:
        flag = 1
        line = index
        break
    index+=1

contents = file.readlines()

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
                file2 = open("Data.txt", 'r')
                #to only print the line which contains data you need to search for the word data in all the lines and then print the line which contains that word
            elif choice == "one":
                website = input("Enter the name for the website for which you want to view your saved credentials:")
                #think of how to solve this
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

    #code for signing up needs to be written