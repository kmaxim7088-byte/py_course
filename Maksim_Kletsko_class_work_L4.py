import copy

# Tranning mind

st = "dkfldkfl;dl;fds"
print(len(st))

li = [1, ]
li.append(32323)
print(li)
print(len(li))
li2 = li.copy() # тоже самое, что и li2 = li[:]

# New Lesson

li2 = copy.deepcopy(li)
li.append(3453)

print(li)
print(li2)

# String

s = "dsfkdlf"
print(s, len(s), type(s), isinstance(s, str))

for index in range(len(s)):
    print(index, s[index])

alf = "abcdefg*-+! "

for char in alf:
    print(char, ord(char))

for i in range(100, 450):
    print(chr(i), end = " ")

# Шифр сдвига - цезарь

print()

print()
print("Оригинальное сообщение:")

message = "Привет, это послание в будущее!"

print(message)

print()
print("Зашифрованное сообщение:")

secured_message = ""
key = 5

for i in message:
    secured_message += chr(ord(i)+key)

print(secured_message)
print()
print("Дешиврование..")

for i in secured_message:
   print(chr(ord(i)-key), end = "")

print()

s = "hello"
text = "HELLOO"

print(s[:2] + text + s[4:])

li = s
print(set(s)) # тусовка букв
print(text.title())

c = "s"
print(c.isalpha())

c = "1"
print(c.isdigit())

url = "hotmail.*"
li = ["com", "ru", "by", "tech", "eu"]
urlList = []

for postfix in li:
    urlList.append(url.replace("*", postfix))

print(urlList)

s = "       ddfdfd       "
print(s.strip()) 
print(s.lstrip())
print(s.rstrip())

