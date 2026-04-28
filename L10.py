class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def __str__(self):
        return f"name: {self.name} | age: {self.age}"    


    def __repr__(self):
        return f"repr name: {self.name} | age: {self.age}"    


    def speak(self, sound):
        return f"{self.name} says {sound}"
    

    def __add__(self, another_dog):
        return self.age + another_dog.age
    

class Bulldog(Dog):
    def walk(self, steps):
        return f"{self.name} ходит {steps} шагов"
    

    def speak(self, sound):
        return f'Bulldog speak\n' + super().speak(sound)


class Terrier(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color


    def __str__(self):
        return super().__str__() + f" | color: {self.color}"        


tom = Terrier("Tom", 2, "Black")
print(tom)
print(tom.speak("БУЭЭЭЭЭ"))

puppy = Bulldog("Puppy", 4)
print(tom+puppy)



# Стэк
class Stack:
    def __init__(self):
        self.__storage = []
    
    
    def push(self, value):
        self.__storage.append(value)
        print("добавляю:", value)
    
    
    def pop(self):
        try:
            res = self.__storage.pop()
            print("удалил:", res)
        except IndexError:
            print("Твой склад пуст")
        except:
            print("Какая-то ошибка")


    def get_stack(self):
        return self.__storage


class Storage:
    def __init__(self):
        self.__items = []


    def priemka(self, value):
        self.__items.append(value)
        print("Приемка товара на склад:", value)

    
    def otgruzka(self):
        try:
            res = self.__items.pop()
            print("Отгрузка товара со склада:", res)
        except IndexError:
            print("Такого товара нет на складе")
        except:
            print("Какая-то ошибка")


    def get_items():
        pass

sklad1 = Stack()
sklad1.pop()
sklad1.push(223)
print(sklad1.get_stack())
sklad1.push(3465)
print(sklad1.get_stack())