# L3
# list
import enum
from locale import currency


numbers = [1, 2, 3, 4, 5, 6]
print(numbers)
print(numbers[1])
print(numbers[0])
print(numbers[5])

# 27.03.2026
# copy
newLi = numbers.copy()
print(numbers, newLi)

a = 1
b = 1
print(id(a), id(b))

del newLi[-1]
print(newLi)

removedVal = newLi.pop()
print(removedVal)

newLi.clear()
print(newLi)

# for in range print input append result sort reverse Len
num = int(input("Сколько чисел хочешь ввести?"))
userList = []

for value in range(num):
    userList.append(int(input("Введи число -->")))
    
resultSum = sum(userList)
print("original =", userList)
userList.sort()
print("sort =", userList)
userList.reverse()
print("reverse =", userList)
print("lenght =", len(userList))
print("sum =", resultSum)

# by value
li = [1,2,3,5,6,8,8]

for value in li:
    print("value =", value, end=" ")

# by index
print()

for index in range(len(li)):
    print("index =", index)
    print("< value >", li[index])

li = ["йа", "бальшой", "маладис", "!"]

for i, value in enumerate(li):
    print(i, value)

currency = ["BYN", "RUB", "USD", "EUR"]
country = ["Belarus", "Russia", "USA", "Le France"]

print(list(zip(currency, country)))

for curr, country in list(zip(currency, country)):
    print(curr, country)

# sort HW 3
liSort = [2, 6, 9, 3, 1]
print("start list =", liSort)

for i in liSort:
    for j in range(len(liSort)-1):
        if liSort[j] > liSort[j+1]:
            temp = liSort[j]
            liSort[j] = liSort[j+1]
            liSort[j+1] = temp

print("end sort list =", liSort)

# startindex:endindex
print(liSort[1:4])

liDublicate = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 1, 2]
print(liDublicate)

se = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 1, 2}
print(se)

li = list(set(liDublicate))
print(li)

# lab 3.4
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print(set(my_list))

# однострочники циклы
st = "skeikdmnskertlghuoyae"
li = []

for char in st:
    if char in "aeoyuqi":
        li.append(char.upper())
    else:
        li.append(char*3)

print(li)

res = [char.upper() for char in st if char in "aeoyuqi"]
print(res)

a, b = map(int, input("Введите два числа через пробел: ").split())

print(a, b)
print(a+b)