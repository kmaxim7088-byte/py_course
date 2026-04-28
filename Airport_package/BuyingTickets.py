import Airport_package.UserProfileData as usData
import Airport_package.OccupiedSeats as seats
import Airport_package.ShoppingCart as cart

flightList = {
    1:{
        "Where": "Moscow",
        "Airplane": "Air150",
        "Capacity": 150,
        "Row": "A-J",
        "Seats": 15
    },
    2:{
        "Where": "Egypt",
        "Airplane": "Boeing350",
        "Capacity": 260,
        "Row": "A-J",
        "Seats": 26
    },
    3:{
        "Where": "Türkiye",
        "Airplane": "SU24",
        "Capacity": 210,
        "Row": "A-J",
        "Seats": 21
    },
    4:{
        "Where": "Greece",
        "Airplane": "AirBus375",
        "Capacity": 180,
        "Row": "A-J",
        "Seats": 18
    },
    5:{
        "Where": "Dubai",
        "Airplane": "MaxAir150",
        "Capacity": 420,
        "Row": "A-J",
        "Seats": 42
    }

}
tariffList = {
    1:{
        "Tariff": "Economy",
        "Price": 150
    },
    2:{
        "Tariff": "Comfort",
        "Price": 300
    },
    3:{
        "Tariff": "Business",
        "Price": 1200
    }
}

buyingList = {}

def flight_selection_menu(userID):
    print("Select your desired flight:")
    print()
    print("1.", flightList[1]["Where"])
    print("2.", flightList[2]["Where"])
    print("3.", flightList[3]["Where"])
    print("4.", flightList[4]["Where"])
    print("5.", flightList[5]["Where"])
    print("6. Back")

    userSelection = int(input("Make a choice --> "))

    if userSelection == 1:
        selection_of_tickets(userID, 1, flightList[1]["Where"])
    elif userSelection == 2:
        selection_of_tickets(userID, 2, flightList[2]["Where"])
    elif userSelection == 3:
        selection_of_tickets(userID, 3, flightList[3]["Where"])
    elif userSelection == 4:
        selection_of_tickets(userID, 4, flightList[4]["Where"])
    elif userSelection == 5:
        selection_of_tickets(userID, 5, flightList[5]["Where"])
    elif userSelection == 6:
        usData.profile_menu(userID)


def selection_of_tickets(userID, flight, where):
    returnDate = False
    discountReturn = 0.08
    discountChild = 0.5
    r = flightList[flight]["Row"]
    s = flightList[flight]["Seats"]

    adultCount = int(input("Number of adults: "))
    childCount = int(input("Number of children (3-6 years old): "))

    print("""
Would you like to purchase round-trip tickets?
          
1. Yes
2. No
""")
    
    if int(input("Make a choice --> ")) == 1:
        returnDate = True

    depDate = input("Desired departure date (dd.mm.yyyy): ") 

    while not checkCorrectInputData(depDate):
        print("Incorrect input")
        depDate = input("Desired departure date (dd.mm.yyyy): ")    

    if returnDate == True:
        discount = 0.1
        retDate = input("Desired return date (dd.mm.yyyy): ")

        while not checkCorrectInputData(retDate):
            print("Incorrect input")
            retDate = input("Desired return date (dd.mm.yyyy): ")

    print(f"""
List of available tariffs:
        
1. {tariffList[1]["Tariff"]}
2. {tariffList[2]["Tariff"]}
3. {tariffList[3]["Tariff"]}
""")
    
    userTariff = int(input("Select your desired tariff --> "))    

    if userTariff == 1:
        priceTariff = tariffList[1]["Price"]
        
        for step in range(adultCount):
            list_places = inputRowAndPlace(flightList[flight]["Airplane"], s, r, step+1, "Adult")
            cart.add_ticket(where, flightList[flight]["Airplane"], depDate, retDate if returnDate else "-", tariffList[1]["Tariff"], "Adult", list_places["row"], list_places["place"], priceTariff, discountReturn if returnDate else 0.)

        for step in range(childCount):
            list_places = inputRowAndPlace(flightList[flight]["Airplane"], s, r, step+1, "Child")
            cart.add_ticket(where, flightList[flight]["Airplane"], depDate, retDate if returnDate else "-", tariffList[1]["Tariff"], "Child", list_places["row"], list_places["place"], priceTariff, discountChild + discountReturn if returnDate else discountChild)

    elif userTariff == 2:
        priceTariff = tariffList[2]["Price"] 

        for step in range(adultCount):
            list_places = inputRowAndPlace(flightList[flight]["Airplane"], s, r, step+1, "Adult")
            cart.add_ticket(where, flightList[flight]["Airplane"], depDate, retDate if returnDate else "-", tariffList[2]["Tariff"], "Adult", list_places["row"], list_places["place"], priceTariff, discountReturn if returnDate else 0.)
            
        for step in range(childCount):
            list_places = inputRowAndPlace(flightList[flight]["Airplane"], s, r, step+1, "Child")
            cart.add_ticket(where, flightList[flight]["Airplane"], depDate, retDate if returnDate else "-", tariffList[2]["Tariff"], "Child", list_places["row"], list_places["place"], priceTariff, discountChild + discountReturn if returnDate else discountChild)

    elif userTariff == 3:
        priceTariff = tariffList[3]["Price"]

        for step in range(adultCount):
            list_places = inputRowAndPlace(flightList[flight]["Airplane"], s, r, step+1, "Adult")
            cart.add_ticket(where, flightList[flight]["Airplane"], depDate, retDate if returnDate else "-", tariffList[3]["Tariff"], "Adult", list_places["row"], list_places["place"], priceTariff, discountReturn if returnDate else 0.)
            
        for step in range(childCount):
            list_places = inputRowAndPlace(flightList[flight]["Airplane"], s, r, step+1, "Child")
            cart.add_ticket(where, flightList[flight]["Airplane"], depDate, retDate if returnDate else "-", tariffList[3]["Tariff"], "Child", list_places["row"], list_places["place"], priceTariff, discountChild + discountReturn if returnDate else discountChild)

    usData.profile_menu(userID)

def checkCorrectInputData(data):
    if data.count(".") != 2 or len(data) != 10:
        return False
    return True


def checkCorrectInputRow(row):
    Row = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}
    return row in Row


def checkCorrectInputPlace(place, s):
    return place > 0 and place <= s


def inputRowAndPlace(airplane, s, r, count, type):
    freeSeats = seats.return_free_and_reserved_seats(airplane, s)
    
    free_seats = ""
    for key, value in freeSeats.items():
        for k, v in value.items():
            if k == "free":
                free_seats += key + ": " + v + "\n"      

    
    print(f"""
Free seats:    
{free_seats}  
    
{count} {type}:
""")
    row = input(f"Specify the row of seats ({r}) --> ")
    while not checkCorrectInputRow(row.upper()):
        print("Incorrect input!")
        row = input(f"Specify the row of seats ({r}) --> ")

    place = int(input(f"Specify location (1-{s}) --> "))
    while not checkCorrectInputPlace(place, s):
        print("Incorrect input!")
        place = int(input(f"Specify location (1-{s}) --> "))    

    while not seats.check_occupied_seat(airplane, row.upper(), place):
        row = input(f"Specify the row of seats ({r}) --> ")
        place = int(input(f"Specify location (1-{s}) --> "))

    seats.add_seat(airplane, row.upper(), place)

    returned_list = {
        "row": row.upper(),
        "place": place
    }

    return returned_list