
# Try except

try:

    #raise ZeroDivisionError
    #raise ValueError
    #raise AttributeError

    cash = int(input("Сумма которую хочешь накопить? "))
    m = int(input("Количество месяцев за которые хочешь накопить сумму? "))
    res = cash / m
    print(f"Тебе нужно откладывать {res} в месяц, чтобы за {m} месяцев накопить {cash}")
except ZeroDivisionError as e:
    print("Делить на 0 нельзя")
    print(e)
    print(e.args)
    print(e.with_traceback)
except ValueError:
    print("Введена строка")
except:
    print("Возникла ошибка")