test_cases = int(input("Enter the number of test cases (input range from 1 to 100): "))
count = 1
again = True

while(again == True):
    if (test_cases < 1) or (test_cases > 100):
        print("ENTER THE VALUE FOR TEST CASES WITHIN THE SPECIFIED RANGE")
        test_cases = int(input("Enter the number of test cases (input range from 1 to 100): "))
    else:
        while(count<=test_cases):
            x = int(input("Enter the monthly cost of the gym (input range from 1 to 100): "))
            y = int(input("Enter the monthly cost for hiring a trainer in the gym (input range from 1 to 100): "))
            z = int(input("Enter the monthly budget of the chef (input range from 1 to 100): "))
            again2 = True
            total = x+y

            while(again2 == True):
                if (x < 1) or (x > 100) or (y < 1) or (y > 100) or (z < 1) or (z > 100):
                    print("ENTER THE VALUE FOR X, Y, Z IN THE SPECIFIED RANGE")
                    x = int(input("Enter the monthly cost of the gym (input range from 1 to 100): "))
                    y = int(input("Enter the monthly cost for hiring a trainer in the gym (input range from 1 to 100): "))
                    z = int(input("Enter the monthly budget of the chef (input range from 1 to 100): "))
                    total = x + y

                else:
                    if (z>=total):
                        print(2)
                    elif (z>=x):
                        print(1)
                    else:
                        print(0)
                    
                    again2 = False
            
            count+=1
        
        again = False