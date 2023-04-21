import csv

user_info = open("User_Info.csv", "r")
data_user_info = list(csv.reader(user_info))
'''print(data_user_info)'''
print("Please enter your login ID and Password")
ID_Attempts = 0
while ID_Attempts == 0:
    ID_input = input("ID: ")
    if ID_input == data_user_info[0][1]:
        Password_Attempts = 3
        while Password_Attempts != 0:
            Password_input = input("Password: ")
            Password_Attempts -= 1
            if Password_input == data_user_info[1][1]:
                print("WELCOME")
                working_type_attempt = 0
                while working_type_attempt == 0:
                    working_type = input("What you want to do (checkin or checkout) ?")
                    if working_type == "checkin":
                        import Checkin

                        break
                    elif working_type == "checkout":
                        import Checkout

                        break
                    else:
                        print("wrong input")
                break
            else:
                print("Wrong Password")
                if Password_Attempts != 0:
                    print(f"{Password_Attempts} attempts remaining")
                else:
                    print("you used your maximum number of attempts, please try after some time")
    else:
        print("Enter a valid ID")
