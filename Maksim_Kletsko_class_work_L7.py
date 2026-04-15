
import ToDoList as u

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
                todos.update(u.create_task(0))    
            else:
                todos.update(u.create_task(max(todos.keys())))
            print()
            print("Задача была добавлена")

        elif operation == 2:
            if len(todos) == 0:
                print("Список задач пуст") 

            else:
                u.view_all_task(todos)

        elif operation == 3:
            print()
            
            try:
                task = todos[int(input("Введите id задачи --> "))]
                u.paste_separator()
                print(u.view_task(task))
                u.paste_separator()
            except:
                u.print_except()

        elif operation == 4:
            try:
                todos[int(input("Введите id задачи --> "))]["completed"] = "Выполнено" if int(input("Введите статус для установки (0 - False, 1 - True) --> ")) == 1 else "Не выполнено"
                print()
                print("Статус был изменен")
            except:
                u.print_except()

        elif operation == 5:
            print()
            try:
                del todos[int(input("Введите id задачи --> "))]
                print()
                print("Задача была удалена")
            except:
                u.print_except()

        print()
        operation = int(input("Выберите действие --> "))


start_app()