
student_class = {}

def main():
    start_Menu = """
    --------------------------------------------------------------------------
                                  Avg Score v1.0

        1. Add a student                 2. Add a mark to a student by ID
      
        3. Delete a student by ID        4. Display a list of students        
                                    
        5. Display the AVG for students  6. Exit

    --------------------------------------------------------------------------
    """

    print(start_Menu)

    userOperation = int(input("Select action --> "))
    
    while userOperation != 6:
        if userOperation == 1:
            student_class.update(add_student(1) if len(student_class) == 0 else add_student(max(student_class.keys())+1))

        elif userOperation == 2:
            try:
                add_mark(student_class[int(input("Enter student ID --> "))])
            except:
                print("Failed to add a mark")

                if len(student_class) == 0:
                    print_except()

        elif userOperation == 3:
            try:
                del student_class[int(input("Enter student ID --> "))]
            except:
                print("Failed to delete student")

                if len(student_class) == 0:
                    print_except()

        elif userOperation == 4:
            
            if len(student_class) == 0:
                print_except()
            else:
                view_list_of_student()

        elif userOperation == 5:
            if len(student_class) == 0:
                print_except()
            else:
                calc_AVG()
                

        userOperation = int(input("Select action --> "))


def add_student(max_id):

    """
    This function adds a student

    Parameters:
    :max_id: Maximum serial number.
    :return: New list entry.
    """

    mark_list = []

    name = input("Enter the student's name --> ")
    user_mark = int(input("Enter the mark (1-10) --> "))

    while not valid_mark_entry(user_mark):
        print("The mark was entered incorrectly")
        user_mark = int(input("Enter the mark (1-10) --> "))

    mark_list.append(user_mark)

    new_student_list = {
        max_id:{
            "name": name,
            "mark": mark_list       
        }  
    }

    return new_student_list


def add_mark(student):
    for k, v in student.items():
        if k == "mark":
             user_mark = int(input("Enter the mark (1-10) --> "))

             while not valid_mark_entry(user_mark):
                print("The mark was entered incorrectly")
                user_mark = int(input("Enter the mark (1-10) --> "))
                
             v.append(user_mark)


def view_list_of_student():

    """
    This function displays a list of students
    """

    for k, v in student_class.items():
        print(f"Student id[{k}]:")
        
        for key, val in v.items():
            print(key + ":", end=" ")

            if key == "name":
                print(val)
            else:
                for mark in val:
                    print(mark, end=", ")


        print()


def calc_AVG():
        
    """
    This function calculates the average score for all students.
    """

    for k, v in student_class.items():
        for key, val in v.items():

            if key == "name":
                print("Student", key + ":", end=" ")
            else:
                sum_mark = 0

                for mark in val:
                    sum_mark += mark
                
                print(round(sum_mark/len(val), 2))


def print_except():
    
    """
    This function throws an exception for an empty student list.
    """

    print("Student list is empty.")
    print("Please, add a student.")


def valid_mark_entry(mark):

    """
    This function checks whether the mark input is correct.

    Parameters:
    :mark: User-entered mark
    :return: Check result (True|False)
    """

    return mark >= 1 and mark <= 10
    

main()