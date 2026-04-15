
def create_task(max_id):
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

def view_all_task(todos):
    print()
    print("Список текущих задач:")

    for k, v in todos.items():
        paste_separator()
        print()
        print("Task", k)
        view_task(v)
    
    paste_separator()


def view_task(task):
    print()
    for k2, v2 in task.items():
            print(k2 + ":", v2)


def paste_separator():
    print()
    print("------------------------------------")      


def print_except():
    print()
    print("Такой задачи не существует!")
