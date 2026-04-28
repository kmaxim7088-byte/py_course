from abc import ABC, abstractmethod

class User:
    __counter = 0
    def __init__(self, name):
        self.user_name = name
        User.__counter += 1

    # альтернативный конмтруктор
    @classmethod
    def init_including_email_age(cls, name, email, age):
        _user = cls(name)
        _user.user_email = email
        _user.user_age = age
        return _user

    def get_name(self):
        return f"{self.user_name}"
    
    def __str__(self):
        return f"{self.user_name}"
    
    def __repr__(self):
        return f"repr User: name: {self.user_name}"

    @classmethod
    def double_counter(cls):
        cls.__counter *= 2

    @classmethod
    def get_counter(cls):
        return cls.__counter
    
    @classmethod
    def set_counter(cls, n):
        cls.__counter += n

    @staticmethod
    def pow_two(n):
        return n**2

dima = User("Dima")
print(dima.get_name())
print(dima)
print(dima.pow_two(2))
print(User.pow_two(5))
User.counter = User.pow_two(2)
User.double_counter()
print(User.counter)
anton = User.init_including_email_age("Anton", "sedfdfsd", 18)
print(anton.__dict__, ">", dima.__dict__)

# Абстрактный класс
class Task_Export_Data(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def export(self):
        pass

    @abstractmethod
    def check(self):
        pass


class json_data(Task_Export_Data):
    def __init__(self, data):
        self.__data = data
    def check(self):
        print("чтото проверяю json")
    def prepare(self):
        print("чтото подготавливаю json")
    def export(self):
        print("чтото экспортирую json")
        print(self.__data)

class pdf_data(Task_Export_Data):
    def __init__(self, data):
        self.__data = data
    def check(self):
        print("чтото проверяю pdf")
    def prepare(self):
        print("чтото подготавливаю pdf ")
    def export(self):
        print("чтото экспортирую pdf")
        print(self.__data)


class csv_data(Task_Export_Data):
    def __init__(self, data):
        self.__data = data
    def check(self):
        print("чтото проверяю csv")
    def prepare(self):
        print("чтото подготавливаю csv")
    def export(self):
        print("чтото экспортирую csv")
        print(self.__data)

li = [csv_data("a, b, c, d, e"), pdf_data("dssfsf sdsfsfs fsfsfs gsd f dg"), json_data("{name: 'stas', age: 44}")]

for inst in li:
    inst.prepare()
    inst.check()
    inst.export()

# MRO
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"repr: name:{self.name} |age:{self.age}"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    def walk(self, steps):
        return f"{self.name} ходит {steps} шагов"

    def speak(self, sound):
        par_speak = super().speak(sound)
        par_speak = par_speak.upper()
        return "Bulldog speak\n" + par_speak

print(Dog.mro())
print(Bulldog.mro())

# свой Except 
# try:
#     1+1
# except:
#     print(1)
# else:
#     print("ошибок нет")
# finally:
#     print("всегда")

# def n():
#     try:
#         1+1
#     except:
#         return False
#     else:
#         return True
#     finally:
#         return 10000

# print(n())

# def n():
#     try:
#         1+1
#     except:
#         return False
#     else:
#         return True
#     finally:
#         print("close.. coonnn")

# print(n())

# class EmptyStorageError(Exception):
#     pass

# class Storage:
#     def __init__(self):
#         self.__items = []

#     def priemka(self, value):
#         self.__items.append(value)
#         print("Приемка товара на склад:", value)

#     def otgruzka(self):
#         if len(self.__items) == 0:
#             raise EmptyStorageError("На складе закончился товар!")
        
#         res = self.__items.pop(0)
#         print("Отгрузка товара со склада:", res)

#     def get_items(self):
#         return self.__items
    

# s = Storage()
# s.get_items()
# s.priemka("Товар 1")
# s.priemka("Товар 2")
# s.priemka("Товар 3")

# s.otgruzka()
# s.otgruzka()
# s.otgruzka()
# s.otgruzka()

class EmptyStorageError(Exception):
    pass

# очередь
# ложим в конец
# достаем с начала
class Storage:
    def __init__(self):
        self.__items = []
    def priemka(self, value):
        self.__items.append(value)
        print("Приемка товара на склад:", value)
    def otgruzka(self):
        if len(self.__items) == 0:
            raise EmptyStorageError("на складе закончился товар!")

        res = self.__items.pop(0)
        print("Отгрузка товара со склада:", res)

def get_items(self):
    return print(self.__items)


class App:
    def __init__(self, storage):
        self.__storage = storage
    def run(self):
        oper = input("1 приемка, 2 отгрузка, 3 вывод всех товаров на складе, 4 exit")
        while oper != "exit":
            if oper == "1":
                self.__storage.priemka(input("введи товар:"))
            elif oper == "2":
                try:
                    self.__storage.otgruzka()
                except EmptyStorageError as e:
                     print("Склад пуст!")
                else:
                    print("Отгрузка прошла успешно.")
            elif oper == "3":
                self.__storage.get_items()
            elif oper == "exit":
                break
            else:
                print("не понимаю")
            oper = input("1 приемка, 2 отгрузка, 3 вывод всех товаров на складе, 4 exit")
        print("poka")

app = App(Storage())
app.run()