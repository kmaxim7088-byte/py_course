
shoppingList = {}

def add_purchase(newList):
    shoppingList.update(newList)


def view_purchases_list():
    totalPay = 0.

    for key, val in shoppingList.items():
        print(str(key) + ": ")

        for k, v in val.items():
            print(k + ":", v)

            if k == "Price":
                totalPay += v

        print("----------")

    print()
    print(f"-----Total price: {totalPay}-----")


def refund_ticket(id):
    del shoppingList[id]


def count_goods():
    return max(shoppingList.keys()) if len(shoppingList) > 0 else 0