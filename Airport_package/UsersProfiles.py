
usersData = {}

def add_new_profile_data(userID, userFirstName, userLastName, userBirthday, userPhone, userEmail):
    global usersData 
    newProfileList = {
                userID: {
                    "FirstName": userFirstName,
                    "LastName": userLastName,
                    "Birthday": userBirthday,
                    "Phone": userPhone,
                    "Email": userEmail
                }
            }

    usersData.update(newProfileList)
    

def profile_data(userID):
    return usersData[userID]


def edit_profile_data(userID, key, value):
    global usersData
    usersData[userID][key] = value


def delete_user_profile(userID):
    global usersData
    del usersData[userID]