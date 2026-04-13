todos = {}

def start_app():
    start_Menu = """
    ----------------------------------------------------------------------------
                                 ToDo manager v1.0

      1. Создать задачу    2. Вывести список задач    3. Получить задачу 
      
      4. Изменить статус   5. Удалить задачу          6. Выход

    ----------------------------------------------------------------------------
    """

    print(start_Menu)

    operation = int(input("Выберите действие --> "))
    print()

    while operation != 6:
        
        if operation == 1:
            if len(todos) == 0:
                todos.update(create_task(0))    
            else:
                todos.update(create_task(max(todos.keys())))
            print()
            print("Задача была добавлена")

        elif operation == 2:
            if len(todos) == 0:
                print("Список задач пуст") 

            else:
                view_all_task()

        elif operation == 3:
            print()
            
            try:
                task = todos[int(input("Введите id задачи --> "))]
                paste_separator()
                print(view_task(task))
                paste_separator()
            except:
                print_except()

        elif operation == 4:
            try:
                todos[int(input("Введите id задачи --> "))]["completed"] = "Выполнено" if int(input("Введите статус для установки (0 - False, 1 - True) --> ")) == 1 else "Не выполнено"
                print()
                print("Статус был изменен")
            except:
                print_except()

        elif operation == 5:
            print()
            try:
                del todos[int(input("Введите id задачи --> "))]
                print()
                print("Задача была удалена")
            except:
                print_except()

        print()
        operation = int(input("Выберите действие --> "))


def create_task(max_id):

    """
    Функция создает задачу

    Описание параметров:
    :max_id: Передается порядковый id задачи.
    :return: Возвращает список с задачей.
    """

    auto_id = max_id + 1

    todo = input("todo: ")
    completed = int(input("completed: "))
    userId = int(input("userId: "))
    priority = int(input("priority: "))

    new_task = {
        auto_id:{
                "todo": todo,
                "completed": "Выполнено" if completed == 1 else "Не выполнено",
                "userId": userId,
                "priority": priority
        }
    }

    return new_task

def view_all_task():
    
    """
    Функция отображает все задачи
    """

    print()
    print("Список текущих задач:")

    for k, v in todos.items():
        paste_separator()
        print()
        print("Task", k)
        view_task(v)
    
    paste_separator()


def view_task(task):

    """
    Функция отображает указанную задачу

    Описание параметров:
    :task: Передается id конкретной задачи.
    """

    print()
    for k2, v2 in task.items():
            print(k2 + ":", v2)


def paste_separator():

    """
    Функция добавляет к выводу разделитель
    """

    print()
    print("------------------------------------")      


def print_except():

    """
    Функция выводит ошибку, если задача не была найдена
    """

    print()
    print("Такой задачи не существует!")

start_app()
help(view_all_task)
help(view_task)