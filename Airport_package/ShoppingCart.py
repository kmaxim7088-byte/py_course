import Airport_package.UserPurchases as purch

shoppingCart = {}

def add_ticket(where, airplane, depDate, retDate, tariff, ticketType, row, place, priceTariff, discount):
    newList = {
        max(shoppingCart.keys()) + 1 if len(shoppingCart) > 0 else 1: {
            "From": "Minsk",
            "Where": where,
            "Airplane": airplane,
            "Departure date": depDate,
            "Return date": retDate,
            "Tariff": tariff,
            "Ticket type": ticketType,
            "Row": row,
            "Place": place,
            "Price": priceTariff - (priceTariff * discount)
        }
    }

    shoppingCart.update(newList)


def return_shopping_cart():
    totalPay = 0.

    for key, val in shoppingCart.items():
        print(str(key) + ": ")

        for k, v in val.items():
            print(k + ":", v)

            if k == "Price":
                totalPay += v

        print("----------")

    print()
    print(f"-----Total price: {totalPay}-----")


def buy_ticket():
    purch.add_purchase(shoppingCart)
    shoppingCart.clear()


def count_goods():
    return max(shoppingCart.keys()) if len(shoppingCart) > 0 else 0