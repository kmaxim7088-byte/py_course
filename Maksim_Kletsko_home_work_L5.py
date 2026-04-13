# HW 5.1

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
        
    return False


def startapp():
    
    test_data = [1500, 1900, 2000, 2016, 1987]
    test_result = [False, False, True, True, False]
    
    for year, result in zip(test_data, test_result):
        if is_year_leap(year) == result:
            print(year, 'is leap -->', result)
        else:
            print(year, 'from your func -->', is_year_leap(year))
            print('but expected -->', result)


print('Високосный' if is_year_leap(int(input("Введите год: "))) == True else 'Обычный')
startapp()

# HW 5.4
   
main_menu = """
--------------------------------------------------------
   
                 Fibonacci numbers v1.0
        ***You need to specify a numerical range 
           to calculate the Fibonacci number*** 

                ***To exit, enter 0***
--------------------------------------------------------
"""   
        
def febo(num):
    if num < 1:
        return None
    if num < 3:
        return 1
    
    return febo(num-1) + febo(num-2)


def febo_test():    
    for i in range(-1, 25):
        print(febo(i))
        

def start_app():    
    print(main_menu)
    print()
    
    a = int(input('Enter the desired number of sequences: '))
    
    while a != 0:
        count = 0
        
        for num in range(0, a):
            count = count + 1
            print(f'fib{count} =', febo(num))
        
        print()
        a = int(input('Enter the desired number of sequences: '))
    

febo_test()
start_app()