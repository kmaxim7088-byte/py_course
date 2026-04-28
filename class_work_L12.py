
# class A:
#     def __init__(self, aa, bb):
#         self._aa = aa
#         self._bb = bb

#     @property
#     #def get_aa(self):
#     def aa(self):
#         print("Сработал метод getter")
#         return self._aa

#     @aa.setter
#     def aa(self, value):
#         print("Сработал метод setter")
#         self._aa = value
#         print("Значение которое устанавливается", value)  

#     @property
#     #def get_aa(self):
#     def bb(self):
#         print("Сработал метод getter")
#         return self._bb

#     @bb.setter
#     def bb(self, value):
#         print("Сработал метод setter")
#         self._bb = value
#         print("Значение которое устанавливается", value)

#     # aa = property(get_aa, set_aa)  

# aaaaa = A(11,22)

# print(aaaaa.aa)
# aaaaa.aa = 5
# print(aaaaa.aa)

# print(aaaaa.bb)
# aaaaa.bb = 23
# print(aaaaa.bb)

# def hhh(*args):
#     return args

# print(hhh(58556))
# print(hhh(58556, 434343, 434535))

# def my_print(*args, m_sep =' ', m_end='\n'):
#     for val in args:
#         print(val, end=m_sep)
#     print(end=m_end)

# my_print(234, 24, 23)
# my_print(234)
# my_print(234, [24, 24, 5], "23")

# di = dict(a=10, b=11, c=16)
# print(di)

# def user(**kwargs):
#     return kwargs

# u1 = user(name = "dima", age=15)
# print(u1)
# print(u1.get("name"))

# def my_math(a,b,c):
#     b = (lambda n: n*2/n**5%7/n*100)(b)
#     return a*b*c

# print((lambda n: n**2)(3))
# print(my_math(2,4,6))

# class Task:
#     def __init__(self, tname, tprior):
#         self.tname = tname
#         self.tprior = tprior
#     def __str__(self):
#         return f"{self.tname} | {self.tprior}"

# class Tasks:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def __iter__(self):
#         return iter(self.tasks)


# tt = Tasks()
# tt.add_task("t1")
# tt.add_task("t1")
# tt.add_task("t1")

# for task in tt.__iter__():
#     print(task)


class pow_two:
    def __init__(self, m=0):
        self.m = m

    def __iter__(self):
        self.c = 0
        return self
    
    def __next__(self):
        if self.c <= self.m:     
            self.c += 1
            return 2 ** self.c
        
        raise StopIteration
        

# p = pow_two(10)

# for i in p:
#     print(i)

# Generator
def num(x):
    for i in range(x):
        yield i
    
user_number = 10

for val in num(user_number):
    print(val, end=" ")

a, b = map(int, input("Vvedite chisla: ").split())
print(a,b)

print(list(zip("ssdsf", range(4), range(5))))

def do_one(x):
    x = 2
    def save():
        return x + 3**2
    return save

res = do_one(4)
print(res())

# метаклассы

print(pow_two.__class__)
print(pow_two.__bases__)

class Task(list):
    def my_append(self, value):
        print("добавляю в список значение", value)
        self.append(value)

    def my_pop(self):
        if len(self) == 0:
            print("Список пустой")
            return
        res = self.pop()
        print("Удаляю значение из списка", res)

ttt = Task()
ttt.my_append(55)
ttt.my_append(5)

My_tasks = type(
    "My_tasks",
    (list,),
    dict(
        my_append=lambda self, value: self.append(value),
        my_pow=lambda self: self.pop(),
    )
)

my_ttt = My_tasks()
print(my_ttt)

tupA = {2, 6}
tupB = {4, 6}
tupC = {6, 51}
tupA = (tupA + tupB + tupC)
print(tupA)

