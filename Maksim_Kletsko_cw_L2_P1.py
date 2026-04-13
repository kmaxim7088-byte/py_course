Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
23true = 4
SyntaxError: invalid decimal literal
help(input)
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

s = input("Привет, как дела?")
Привет, как дела?Cупер
ы
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ы
NameError: name 'ы' is not defined
s
'Cупер'
print(f"Меня зовут {s}")
Меня зовут Cупер
type(s)
<class 'str'>
casting s
SyntaxError: invalid syntax
age = int(input('Сколько тебе лет?')
print(age/2)
          
SyntaxError: '(' was never closed
age = int(input('Сколько тебе лет?'))
print(age/2)
          
SyntaxError: multiple statements found while compiling a single statement
age = int(input('Сколько тебе лет?'))
          
Сколько тебе лет?23
print(age/2)
          
11.5
isistance
          
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    isistance
NameError: name 'isistance' is not defined. Did you mean: 'isinstance'?
isinstance(a, int)
          
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    isinstance(a, int)
NameError: name 'a' is not defined
isinstance(age, int)
          
True
2 ** 2
          
4
2**3
          
8
2 ** 3 ** 2
          
512

"xa" * 3
          
'xaxaxa'
"Привет" + " " + "Как оно?" + "Норм," + "" + "ха";3
          
'Привет Как оно?Норм,ха'
3
"Привет" + " " + "Как оно?" + " Норм," + "" + "ха"*3
          
'Привет Как оно? Норм,хахаха'
"Привет" + " " + "Как оно?" + " Норм," + "" + " ха"*3
          
'Привет Как оно? Норм, ха ха ха'
name = "Maksim"
          
age = 26
          
phone = "+375291671678"
          
print(f"{name} {age} {phone}")
          
Maksim 26 +375291671678
import keyboard
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    import keyboard
ModuleNotFoundError: No module named 'keyboard'
>>> keyboard.kwlist
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    keyboard.kwlist
NameError: name 'keyboard' is not defined
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a, b = map(float, input("Введите два числа через пробел: ").split())
Введите два числа через пробел: 5 6
>>> print(a+b, a-b, a/b, a*b)
11.0 -1.0 0.8333333333333334 30.0
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
