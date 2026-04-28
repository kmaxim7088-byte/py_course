# import pickle as p
import xml.etree.ElementTree as et

# # fstream = open("users.txt", "wt", encoding="utf-8")
# fstream = open("users.txt", "rt", encoding="utf-8")
# strings = fstream.readlines()
# fstream.close()

# print(strings)
# strings.pop()
# strings.pop()
# strings.pop()
# strings.pop(3)
# strings.pop(5)
# strings.pop(2)
# strings.append("\nЧе ты лысый? ))")
# print(strings)

# newfstream = open("user2.txt", "wt", encoding="utf-8")
# newfstream.writelines(strings)
# newfstream.close()

# newfstream = open("user2.txt", "rt", encoding="utf-8")
# newstrings = newfstream.readlines()
# print(newstrings)


# newlist = ["fdgdg", "fdgfgfgh", "kfkfdlfdlds"]
# newfstream1 = open("user3.txt", "wt", encoding="utf-8")
# newfstream1.writelines(newlist)
# newfstream1.close()

# textfiles = open("text.txt", "at", encoding="utf-8")

sep = "\n"
# reslist = []

# for text in newlist:
#     reslist.append(text+sep)

# textfiles.writelines(reslist)
# textfiles.close()

# s_number = int(input("Сколько строк хочешь ввести в файл? "))

# for i in range(s_number):
#     newfstream = open("interactive.txt", "at", encoding="utf-8") 
#     user_text = str(i) + " " + input("Введите желаемую строку: ") + sep

#     newfstream.write(user_text)
#     newfstream.close()

# # with
# newfstream = open("with_test.txt", "at", encoding="utf-8")
# newfstream.write("fkdkfkdlkofdsk\n")
# newfstream.close()

# with open("with_test.txt", "wt", encoding="utf-8") as newfstream:
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")
#     newfstream.write("fkdkfkdlkofdsk\n")

# pickle
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"user: {self.name} {self.age}"
    
#     def __repr__(self):
#         return f"user: {self.name} {self.age}"
    
# d1 = User("D", 1)
# k1 = User("K", 1)

# with open("data_pickle.txt", "wt") as fs:
#     p.dump(k1, fs)

tree = et.parse("books.xml")
root_element = tree.getroot()
print(root_element.tag)
print(root_element.text)

for sub in root_element:
    print(sub.tag, sub.attrib)

for sub in root_element:
    print(sub.tag, sub.get("title"))
    for sub_sub in sub:
        print(sub_sub.tag, sub_sub.text)    
    print()

print(root_element[0][0].text)

for sub in root_element.findall("book"):
    print(sub.get("title"))