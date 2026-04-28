import Airport_package.Authorization as auth
import Airport_package.UsersProfiles as profile
import Airport_package.UserProfileData as uData
import Airport_package.InputProfileData as inProfData
import pwinput as pw

def main():
    print("""
    ------------------------------------------------------------
                        Welcom to MaxAirline!
    
        1. Login            2. Register              3. Exit               

    ------------------------------------------------------------
    """)

    userSelection = int(input("Please, select an action --> "))

    while userSelection != 3:
        if userSelection == 1:

            userEmail = input("Email: ")
            userPassword = pw.pwinput("Password: ", "*")

            statusAuth = auth.user_auth(userEmail, userPassword)

            while statusAuth == "Incorrect password":
                print(statusAuth)
                userPassword = pw.pwinput("Password: ", "*")
                statusAuth = auth.user_auth(userEmail, userPassword)

            try:    
                uData.profile_menu(int(statusAuth)) 
                break
            except:
                print(statusAuth)

        elif userSelection == 2:
            
            inputData = inProfData.add_profile_data()

            userID = auth.user_register(inputData["Email"], inputData["Password"]) 
            profile.add_new_profile_data(userID, inputData["FirstName"], inputData["LastName"], inputData["Birthday"], inputData["Phone"], inputData["Email"])

            uData.profile_menu(userID)
            break

        userSelection = int(input("Please, select an action --> "))     

    if userSelection != 3:
        main()


main()    