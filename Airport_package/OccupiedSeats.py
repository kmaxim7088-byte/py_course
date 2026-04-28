
occupiedSeatList = {}

def add_seat(airplane, row, place):
    newList = {
        max(occupiedSeatList.keys()) + 1 if len(occupiedSeatList) > 0 else 1:{
            "Airplane": airplane,
            "Row": row,
            "Place": place
        }
    }

    occupiedSeatList.update(newList)


def check_occupied_seat(airplane, row, place):
    planeFound = False
    rowFound = False

    for k, v in occupiedSeatList.items():
        for key, val in v.items():
            if key == "Airplane":
                if val == airplane:
                    planeFound = True
                else:
                    planeFound = False
            if key == "Row" and planeFound:
                if val == row:
                    rowFound = True
                else:
                    rowFound = False
            if key == "Place" and planeFound and rowFound:
                if val == place:
                    print("Place reserved")
                    return False
    
    return True


def return_free_and_reserved_seats(airplane, s):
    airplaneFound = False
    occupiedSeat = {
        "A": {
            "reserved": [],
            "free": ""
        },
        "B": {
            "reserved": [],
            "free": ""
        },
        "C": {
            "reserved": [],
            "free": ""
        },
        "D": {
            "reserved": [],
            "free": ""
        },
        "E": {
            "reserved": [],
            "free": ""
        },
        "F": {
            "reserved": [],
            "free": ""
        },
        "G": {
            "reserved": [],
            "free": ""
        },
        "H": {
            "reserved": [],
            "free": ""
        },
        "I": {
            "reserved": [],
            "free": ""
        },
        "J": {
            "reserved": [],
            "free": ""
        }
    }
    
    for key, val in occupiedSeatList.items():
        row = ""
        seat = 0
        for k, v in val.items():
            if k == "Airplane":
                if v == airplane:
                    airplaneFound = True
                else: airplaneFound == False

            if k == "Row" and airplaneFound:
                row = v
            
            if k == "Place" and airplaneFound:
                seat = v

            if row != "" and seat != 0 and airplaneFound:
                occupiedSeat[row.upper()]["reserved"].append(seat)

    for key2, val2 in occupiedSeat.items():
        freeSeats = []
        for i in range(s):
            freeSeats.append(i+1)
        for k2, v2 in val2.items():
            if k2 == "reserved":
                for pl in v2:
                    freeSeats.remove(pl)

        for free in freeSeats:
            occupiedSeat[key2]["free"] += str(free) + ", "

    return occupiedSeat    