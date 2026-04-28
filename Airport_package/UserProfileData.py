import Airport_package.InputProfileData as inProfile
import Airport_package.Authorization as auth
import Airport_package.UsersProfiles as userprofile
import Airport_package.BuyingTickets as buy
import Airport_package.UserPurchases as buying
import Airport_package.ShoppingCart as cart
import time
import random
import pwinput as pw

userData = {}

def profile_menu(userID):
    userData.clear()
    userData.update(userprofile.profile_data(userID))
    firstName = userData["FirstName"]
    lastName = userData["LastName"]

    print(f"""
    ------------------------------------------------------------
                        Welcom to MaxAirline, 
                           {firstName} {lastName}!
    
       1. My profile    2. Buying tickets   3. My purchases  
                 4. My cart           5. Loggout 
    ------------------------------------------------------------
    """)    

    userSelection = int(input("Please, select an action --> "))

    if userSelection == 1:
        my_profile_info_menu(userID)
    elif userSelection == 2:
        buy.flight_selection_menu(userID)      
    elif userSelection == 3:
        view_user_purcheses(userID)
    elif userSelection == 4:
        view_user_cart(userID)
    elif userSelection == 5:
        userData.clear()
        print(f"See you again, {firstName} {lastName}!")
        

    
def my_profile_info_menu(userID):
    print(f"""
    Name: {userData['FirstName']}
    Surname: {userData['LastName']}
    Date of birthday: {userData['Birthday']} 
    Phone number: {userData['Phone']} 
    Email address: {userData['Email']} 

    1. Edit your profile data
    2. Delete account
    3. Back 
    """)

    userSelection = int(input("Please, select an action --> "))

    if userSelection == 1:
        edit_profile(userID)    
    elif userSelection == 2:
        auth.delete_account(userID)
        userprofile.delete_user_profile(userID)
        print("The account has been deleted")    
    elif userSelection == 3:
        profile_menu(userID)


def edit_profile(userID):
    print("""  
        About me:  

        1. Name
        2. Surname
        3. Date of birthday
        4. Phone
        5. Password
        6. Back
              
        What do you want to change?
    
    """)

    userSelection = int(input("Please, select an action --> "))

    if userSelection == 1:
        value = inProfile.edit_profile_data(userID, "FirstName", "Enter new name: ")
        userData["FirstName"] = value
    if userSelection == 2:
        value = inProfile.edit_profile_data(userID, "LastName", "Enter new surname: ")
        userData["LastName"] = value
    if userSelection == 3:
        value = inProfile.edit_profile_data(userID, "Birthday", "Enter new date of birthday (dd.mm.yyyy): ")
        userData["Birthday"] = value
    if userSelection == 4:
        value = inProfile.edit_profile_data(userID, "Phone", "Enter new phone number (+): ")
        userData["Phone"] = value
    if userSelection == 5:
        value = inProfile.edit_profile_data(userID, "Password", "Enter new password: ")
        userData["Password"] = value

    my_profile_info_menu(userID)


def view_user_cart(userID):
    count = cart.count_goods()
    print("Your cart:\n")
    cart.return_shopping_cart()
    
    print("""
    1. Pay
    2. Back
    """)

    userSelection = int(input("Your choice --> "))

    if userSelection == 1:
        if count > 0:
            input_cart_data(userID)
        else: 
            print("\n Your cart is empty!\n")
            view_user_cart(userID)

    if userSelection == 2:
        profile_menu(userID)


def view_user_purcheses(userID):
    count = buying.count_goods()
    print("Your purcheses:\n")
    buying.view_purchases_list()
    
    print("""
    1. Ticket refund
    2. Back
    """)

    userSelection = int(input("Your choice --> "))

    if userSelection == 1:
        if count > 0:
            ticketID = int(input("Enter ticket number --> "))
            refund_ticket_menu(userID, ticketID)
        else:
            print("\n Your purcheses is empty!\n")
            view_user_purcheses(userID)

    elif userSelection == 2:
        profile_menu(userID)


def input_cart_data(userID):
    card_number = input("Card number: ")
    validity_period = input("Validity period (mm/yy): ")
    cvv = int(pw.pwinput("CVV code: ", "*"))
    owner = input("Owner card: ")

    print("\nPlease wait..")
    time.sleep(random.randint(3, 8))

    cart.buy_ticket()
    print("Payment completed!\n")

    view_user_cart(userID)


def refund_ticket_menu(userID, ticketID):
    buying.refund_ticket(ticketID)
    print("\nPlease wait..")
    time.sleep(random.randint(3, 8))
    view_user_purcheses(userID)