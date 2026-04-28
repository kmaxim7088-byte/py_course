
logDate = {}

def user_auth(email, password):
    userEmail = False
    userPassword = False
    userID = 0

    for k, v in logDate.items():
        for key, value in v.items():
            if key == "Email":
                if value == email:
                    userEmail = True

            if key == "Password" and userEmail == True:
                if value == password:
                    userPassword = True
        
        if userEmail == True and userPassword == True:
            userID = k
            break

    if userID > 0:
        return str(userID)
    elif userEmail == True and userPassword == False:
        return "Incorrect password"
        
    return "User not found"


def user_register(userEmail, userPassword):
    global logDate

    userID = max(logDate.keys()) + 1 if len(logDate) > 0 else 1

    newLogList = {
        userID: {
            "Email": userEmail,
            "Password": userPassword
        }
    }

    logDate.update(newLogList)

    return userID


def edit_user_password(userID, value):
    global logDate
    logDate[userID]["Password"] = value


def delete_account(userID):
    global logDate
    del logDate[userID]