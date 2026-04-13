from re import match
import time


print(1234)
print(1, 2, 3, 4, 5, sep=")")
age = 999
print(age)
type(age)
print(isinstance(age, int))
number = int(input("Enter a number: "))

password = "12345"

print("Окэй") if password == "12345" else print("Нэ Окэй")

age = 0.5
if age <= 1:
    print("Джун")
elif age <= 3:
    print("Мидл")
elif age <= 6:
    print("Сеньор")
else:
    print("Тим лид")

#Версия Python 3.9, нужна 3.10+
# match age:
#     case age if age <= 1:
#         print("Джун")
#     case age if age <= 3:
#         print("Мидл")
#     case age if age <= 6:
#         print("Сеньор")
#     case _:
#         print("Тим лид")

counter = 1
while counter <= number:
    print("Пазишен намбер", counter)
    counter += 1

even, odd = 0, 0
number = int(input("Enter a number or 0 on exit: "))

while number != 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = int(input("Enter a number or 0 on exit: "))

print("Even =", even)
print("Odd =", odd)

for number in range(1, 10, 2):
    print(number, end=" ")

print()

for i in range(5):
    time.sleep(1)
    print("Привет соня!", i)
print()

# break continue
for i in range(5):
   if i == 3:
       break
   print("Привет соня!", i)
print()

for i in range(5):
   if i == 3:
       continue
   print("Привет соня!", i)
print()

HP = 100
time_limit = 60

while time_limit >= 0:

    if HP <= 0:
        break

    print("time limit", time_limit)
    print("У вас осталось HP:", HP)
    if time_limit % 2 == 0:
        # нам дали в голову
        HP -= 15
        print("Вы потеряли от удара в голову 15 HP")
    if time_limit % 2 != 0:
        # нам дали в ногу
        HP -= 5
        print("Вы потеряли от удара в ногу 5 HP")
    print()
    time_limit -= 1

# in not in
text = "wewrtddfdgg"
for char in text:
    print(char.upper()*7)

# and or not
name = "Maksim"
phone = "123"
age = 26

if name == "Maksim" and phone == "123" and age == 26:
    print("Гуд ворк, мистер Пиклз")

if name == "Maksim" or phone == "123" or age == 26:
    print("Гуд ворк, мистер Пиклз")