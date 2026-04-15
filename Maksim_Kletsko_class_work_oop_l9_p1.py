# OOP
# 15 04 2026

class Car:
    pass

class Wallet:
    pass

class House:
    pass

class Person:
    def __init__(self, person_name, person_phone, person_email):
        self.name = person_name
        self.ph = person_phone
        self.email = person_email

mycar = Car()
mywal = Wallet()

maks = Person("Maksim", "24423334", "sdsff@gmail.com")

print(f"name: {maks.name}")
print(f"phone: {maks.ph}")
print(f"email: {maks.email}")