import Airport_package.UsersProfiles as profile
import Airport_package.Authorization as auth
import pwinput as pw

def add_profile_data():

    userFirstName = input("Enter your First name: ")
    userLastName = input("Enter your Last name: ")

    userBirthday = input("Enter your Birthday (dd.mm.yyyy): ")
    while checkIncorrectInput("Birthday", userBirthday) == "Incorrect input":
        userBirthday = input("Enter your Birthday (dd.mm.yyyy): ")

    userPhone = input("Enter your Phone (+): ")
    while checkIncorrectInput("Phone", userPhone) == "Incorrect input":
        userPhone = input("Enter your Phone (+): ")

    userEmail = input("Enter your email: ")
    while checkIncorrectInput("Email", userEmail) == "Incorrect input":
        userEmail = input("Enter your email: ")    

    userPassword = pw.pwinput("Enter your password: ", "*")

    inputUserData = {
        "FirstName": userFirstName,
        "LastName": userLastName,
        "Birthday": userBirthday,
        "Phone": userPhone,
        "Email": userEmail,
        "Password": userPassword, 
    }

    return inputUserData


def checkIncorrectInput(key, userInput):

    correct = False

    if key == "Birthday":
        if userInput.count(".") != 2 or len(userInput) != 10:
            print("Incorrect date of birth") 
        else:
            correct = True            
    elif key == "Phone":
        if "+" not in userInput or len(userInput) < 12:
            print("Incorrect phone number") 
        else:
            correct = True
    elif key == "Email":
        domain = (".ru", ".com", "by")
        correctDomain = False

        if "@" not in userInput:
            print("Incorrect email")
        else:
            for v in domain:
                if v in userInput:
                    if len(userInput) > 12:
                        correctDomain = True
                        correct = True
                        break
            
            if correctDomain != True:
                print("Incorrect email")

    return "Correct input" if correct == True else "Incorrect input"


def edit_profile_data(userID, key, message):
    value = input(message)

    if key == "Birthday" or key == "Phone":
        while checkIncorrectInput(key, value) == "Incorrect input":
            value = input(message)    

    if key != "Password":
        profile.edit_profile_data(userID, key, value)
    else:
        auth.edit_user_password(userID, value)
        
    return value