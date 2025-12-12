import os
# Translition
import time
# Adding colors
from colorama import Fore, Style
def OO2():
    os.system('cls')
    print("==================================================")
    OO1 = ("\tWELCOME TO WORLD OF PYTHON")
    print(Fore.BLUE + OO1 + Style.RESET_ALL)
    time.sleep(0.1)
    print("==================================================")
    OOP = input("\nENTER YOUR NAME ===> ")
    os.system('cls')
    OO2 = input(f"\nHello {OOP}, would you like to learn python? (yes/no)").lower()
    time.sleep(0.1)
    if OO2 == 'yes':
        print("Great choice, let's us begin")
    else:
        print("SYSTEM SHUTTING DOWN")
# Introduction to pyhton
def OO3():
    print('''Python's syntax is designed to be readable and
straightforward. It uses indentation to define the
scope of loops, functions, and classes, unlike
other languages that use curly braces or keywords.''')
    time.sleep(0.1)
    print("Create a funtion using 'print' used to display output")  
    time.sleep(0.1)
    print("on the screen, then type this - ('hello world') -.")
    time.sleep(0.1)
    print('\nExample:\nprint("hello world")')
    time.sleep(0.1)
    print("Test your self\n")
    
    ot = input((Fore.GREEN + '\n>'+ Style.RESET_ALL))
    print('OUTPUT\nHello world\n\n Well done!!1')
    time.sleep(0.5)
    re = input((Fore.RED + "Press Enter to retrun...." + Style.RESET_ALL))
    time.sleep(0.1)
    os.system('cls')

# Variables
def OO4():
    while True:
        from colorama import Fore, Style
        data = (Fore.GREEN + "VARIABLES" + Style.RESET_ALL)
        print(f'[]==================[]{data}[]==================[]')
        print("\tA - Definition of Variables")
        time.sleep(0.1)
        print("\tB - No Declaration Needed ")
        time.sleep(0.1)
        print("\tC - Multiple Assignments ")
        time.sleep(0.1)
        print("\tD - Variable Naming Rules ")
        time.sleep(0.1)
        print("\tE - Type Casting ")
        time.sleep(0.1)
        print("\tF - Examples of Common Variable Types ")
        time.sleep(0.1)
        print('[]================================================[]')
    
        re = (input("Select A - F slides or R to return to menu ----> ")).lower()
        time.sleep(0.1)
        
        if re == 'a':
            os.system('cls')
            O1 = ((Fore.BLACK +"DEFINITION OF VARIABLES"+ Style.RESET_ALL))
            time.sleep(0.1)
            print("In Python, variables are used to store data values.")
            time.sleep(0.1)
            print("Python is a dynamically-typed language, meaning you don't")
            time.sleep(0.1)
            print("need to declare the type of a variable explicitly—it is")
            time.sleep(0.1)
            print("inferred based on the value assigned.")
            time.sleep(0.1)
            col = ((Fore.BLUE + "Key Features of Python Variables" + Style.RESET_ALL))
            time.sleep(0.1)
            print("Dynamic Typing:\nx = 10       # Integer\nx = 'Hello'  # String")
            time.sleep(0.1)

            ret = input((Fore.RED + "Press enter to return..." + Style.RESET_ALL))
            time.sleep(0.1)
            os.system('cls')
    
        elif re == "b":
            os.system('cls')
            col = ((Fore.BLUE + "Key Features of Python Variables" + Style.RESET_ALL))
            time.sleep(0.1)
            print("No Declaration Needed: Variables are created when you\nassign a value to them.")
            time.sleep(0.1)
            print('name = "Alice"\nage = 25')
            time.sleep(0.1)

            re = input((Fore.RED + "Press Enter to retrun...." + Style.RESET_ALL))
            time.sleep(0.1)
            os.system('cls')
        
        elif re == 'c':
            os.system('cls')
            col = ((Fore.BLUE + "Key Features of Python Variables" + Style.RESET_ALL))
            time.sleep(0.1)
            print("Multiple Assignments:\nAssign multiple variables in one line:")
            time.sleep(0.1)
            print("a, b, c = 1, 2, 3\nAssign the same value to multiple variables:")
            time.sleep(0.1)
            print("x = y = z = 100")
            time.sleep(0.1)

            re = input((Fore.RED + "Press Enter to retrun...." + Style.RESET_ALL))
            time.sleep(0.1)
            os.system('cls')

        elif re == 'd':
            os.system('cls')
            col = ((Fore.BLUE + "Key Features of Python Variables" + Style.RESET_ALL))
            time.sleep(0.1)
            print("Variable Naming Rules:")
            time.sleep(0.1)
            print("+ Must start with a letter or an underscore (_).")
            time.sleep(0.1)
            print("+ Cannot start with a number.")
            time.sleep(0.1)
            print("+ Can only contain alphanumeric characters and underscores (A-Z, a-z, 0-9, _).")
            time.sleep(0.1)
            print("+ Case-sensitive (myVar and myvar are different).")
            time.sleep(0.1)

            re = input((Fore.RED + "Press Enter to retrun...." + Style.RESET_ALL))
            time.sleep(0.1)
            os.system('cls')
        
        elif re == 'e':
            os.system('cls')
            col = ((Fore.BLUE + "Key Features of Python Variables" + Style.RESET_ALL))
            time.sleep(0.1)
            print("Type Casting:\nYou can explicitly convert variables to a specific type.")
            time.sleep(0.1)
            print('''x = str(10)   # Converts integer to string
y = int("20") # Converts string to integer
z = float(5)  # Converts integer to float''')
            time.sleep(0.1)

            re = input((Fore.RED + "Press Enter to retrun...." + Style.RESET_ALL))
            time.sleep(0.1)
            os.system('cls')
        
        elif re == 'f':
            os.system('cls')
            print(Fore.BLUE + "Examples of Common Variable Types" + Style.RESET_ALL)
            time.sleep(0.1)
            print("Integer\nnum = 42")
            time.sleep(0.1)
            print("Float:\npi = 3.14")
            time.sleep(0.1)
            print('String:\ngreeting = "Hello, World!"')
            time.sleep(0.1)
            print("Boolean:\nis_active = True")
            time.sleep(0.1)
            print('List:\nfruits = ["apple", "banana", "cherry"]')
            time.sleep(0.1)
            print('Dictionary:\nperson = {"name": "Alice", "age": 25}')
            time.sleep(0.1)

            re = input((Fore.RED + "Press Enter to retrun...." + Style.RESET_ALL))
            time.sleep(0.1)
            os.system('cls')

        elif re == 'r':
            os.system('cls')
            return

# Data Types
def OO5():
    while True:
        os.system('cls')
        from colorama import Fore, Style
        data = (Fore.GREEN + "DATA TYPES" + Style.RESET_ALL)

        print(f'[]==================[]{data}[]==================[]')
        print("\tA - Definition of Data Types")
        time.sleep(0.1)
        print("\tB - Text Types")
        time.sleep(0.1)
        print("\tC - Numeric Types")
        time.sleep(0.1)
        print("\tD - Sequence Types")
        time.sleep(0.1)
        print("\tE - Mapping Types ")
        time.sleep(0.1)
        print("\tF - Boolean Type ")
        time.sleep(0.1)
        print('[]================================================[]')

        sel = (input("Select A - F slides or R to return to menu ----> ")).lower()
        time.sleep(0.1)
        
        if sel == 'a':
            os.system('cls')
            print('''Definition of Data Types Python has a variety
of built-in data types that allow you to work with
different kinds of data effectively.''')
            time.sleep(0.1)

            ret = input(Fore.RED  + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'b':
            os.system('cls')
            print(Fore.BLUE + "TEXT TYPES" + Style.RESET_ALL)
            time.sleep(0.1)
            print('str: Represents a sequence of characters (e.g., "Hello, World!").')
            time.sleep(0.1)
            print('Here another example:\nprint ("Hello World! ")\n Output:\nHello world')
            time.sleep(0.1)

            ret = input(Fore.RED  + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'c':
            os.system('cls')
            print(Fore.BLUE + "NUMERIC TYPES" + Style.RESET_ALL)
            time.sleep(0.1)
            print("int: Integer values (e.g., 42, -7).")
            time.sleep(0.1)
            print("float: Floating-point numbers (e.g., 3.14, -0.001).")
            time.sleep(0.1)

            ret = input(Fore.RED  + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'd':
            os.system('cls')
            print(Fore.BLUE + "SEQUENCE TYPES" + Style.RESET_ALL)
            time.sleep(0.1)
            print("list: Ordered, mutable collection (e.g., [1, 2, 3]).")
            time.sleep(0.1)
            print("range: Represents a sequence of numbers (e.g., range(5)).")
            time.sleep(0.1)

            ret = input(Fore.RED  + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'e':
            os.system('cls')
            print(Fore.BLUE + "MAPPING TYPES" + Style.RESET_ALL)
            time.sleep(0.1)
            print('ict: Key-value pairs (e.g., {"name": "Alice", "age": 25}).')
            time.sleep(0.1)

            ret = input(Fore.RED  + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'f':
            os.system('cls')
            print(Fore.BLUE + "BOOLEAN TYPES" + Style.RESET_ALL)
            time.sleep(0.1)
            print("Represents True or False.")
            time.sleep(0.1)
            print("Logical operators like and, or, and not are used with Boolean values.")
            time.sleep(0.1)
            print("print(True and False)  # Output: False")
            time.sleep(0.1)
            print("print(True or False)   # Output: True")
            time.sleep(0.1)
            print("print(not True)        # Output: False")
            time.sleep(0.1)

            print(Fore.BLUE + "Comparisons Boolean values." + Style.RESET_ALL)
            time.sleep(0.1)
            print("print(5 > 3)   # Output: True")
            time.sleep(0.1)
            print("print(2 == 3)  # Output: False")
            time.sleep(0.1)
            print("print(4 <= 4)  # Output: True")
            time.sleep(0.1)
            
            ret = input(Fore.RED  + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'r':
            os.system('cls')
            return

# Operators
def OO6():
        while True:
            os.system('cls')
            data = (Fore.GREEN + "Operatotrs" + Style.RESET_ALL)
            print(f'[]==================[]{data}[]==================[]')
            print("\tA - Definition of Operators")
            time.sleep(0.1)
            print("\tB - Arithmetic Operators")
            time.sleep(0.1)
            print("\tC - Comparison Operators")
            time.sleep(0.1)
            print("\tD - Logical Operators")
            time.sleep(0.1)
            print("\tE - Assignment Operators")
            print('[]================================================[]')

            sel = (input("Select A - E slides or R to return to menu ----> ")).lower()
            time.sleep(0.1)

            if sel == 'a':
                os.system('cls')
                print('''In Python, operators are special symbols or keywords
used to perform operations on variables and values.
They are categorized into several types based on their
functionality:''')
                time.sleep(0.1)
                ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
                time.sleep(0.1)
                os.system('cls')
            
            elif sel == 'b':
                os.system('cls')
                print(Fore.BLUE + "ARITHMETIC OPERATORS\n" + Style.RESET_ALL)
                time.sleep(0.1)
                print("Used for basic mathematical operations:\n")
                time.sleep(0.1)
                print("+ : Addition (a + b)")
                time.sleep(0.1)
                print("- : Subtraction (a - b)")
                time.sleep(0.1)
                print("* : Multiplication (a * b)")
                time.sleep(0.1)
                print("/ : Division (a / b)")
                time.sleep(0.1)
                print("% : Modulus (remainder, a % h)")
                time.sleep(0.1)
                print("** : Exponentiation (a ** b)")
                time.sleep(0.1)
                print("// : Floor division (a // b)")
                time.sleep(0.1)
                
                
                print("Here some Exmpale of an actual code using Arithrmetic operators:\n")
                time.sleep(0.1)
                print('''n1 = eval(input("Enter the amount of deposit : 10000 "))
print("Here is the breakdown  of the deposit : ")
n2 = n1')
a = n2 // 1000
n2 = n2 % 1000
s = n2 // 500
n2 = n2 % 500
d = n2 // 200
n2 = n2 % 200
f = n2 // 100
n2 = n2 % 100
g = n2 // 50
n2 = n2 % 50
h = n2 // 20
n2 = n2 % 20
j = n2 // 10
n2 = n2 % 10
k = n2 // 5
n2 = n2 % 5
l = n2 // 1
n2 = n2 % 1
print("1000 :",a)
print("500 :",s)
print('print("200 :",d)
print('print("100 :",f)
print('print("50 :",g)
print('print("20 :",h)
print('print("10 :",j)
print('print("5 :",k)
print('print("1 :",l)\n''')
                time.sleep(0.1)

                print(Fore.GREEN + "OUTPUT\n" + Style.RESET_ALL)
                time.sleep(0.1)
                print("1000 : 10")
                time.sleep(0.1)
                print("500 : 0")
                time.sleep(0.1)
                print("200 : 0")
                time.sleep(0.1)
                print("100 : 0")
                time.sleep(0.1)
                print("50 : 0")
                time.sleep(0.1)
                print("20 : 0")
                time.sleep(0.1)
                print("10 : 0")
                time.sleep(0.1)
                print("5 : 0")
                time.sleep(0.1)
                print("1 : 0\n")
                time.sleep(0.1)

                ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
                time.sleep(0.1)
                os.system('cls')
            
            elif sel == 'c':
                os.system('cls')
                print(Fore.BLUE + "COMPARISON OPERATORS\n" + Style.RESET_ALL)
                time.sleep(0.1)
                print("Used to compare two values and return a Boolean (True or False):\n")
                time.sleep(0.1)
                print("== : Equal to (a == b)")
                time.sleep(0.1)
                print("!= : Not equal to (a != b)")
                time.sleep(0.1)
                print("> : Greater than (a > b)")
                time.sleep(0.1)
                print("< : Less than (a < b)")
                time.sleep(0.1)
                print(">= : Greater than or equal to (a >= b)")
                time.sleep(0.1)
                print("<= : Less than or equal to (a <= b)\n")
                time.sleep(0.1)
                print("Here some Exmpale of an actual code using Comparison Operators\n")
                time.sleep(0.1)
                print("a = 10 " "b = 20")
                time.sleep(0.1)

                print("print(a == b) # Output: False")
                time.sleep(0.1)
                print("print(a != b) # Output: True")
                time.sleep(0.1)
                print("print(a > b) # Output: False")
                time.sleep(0.1)
                print("print(a < b) # Output: True")
                time.sleep(0.1)
                print("print(a >= b) # Output: False")
                time.sleep(0.1)
                print("print(a <= b) # Output: True\n")
                time.sleep(0.1)
                ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
                time.sleep(0.1)
                os.system('cls')

            elif sel == 'd':
                os.system('cls')
                print(Fore.BLUE + "LOGICAL OPERATORS" + Style.RESET_ALL)
                time.sleep(0.1)
                print('''Logical operators are used to combine conditional statements.
They include and, or, and not.\nHere are some examples:\n''')
                time.sleep(0.1)
                print("a = True")
                time.sleep(0.1)
                print("b = False")
                time.sleep(0.1)
                print("print(a and b) # Output: False")
                time.sleep(0.1)
                print("print(a or b) # Output: True")
                time.sleep(0.1)
                print("print(not a) # Output: False")
                time.sleep(0.1)

                ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
                time.sleep(0.1)
                os.system('cls')

            elif sel == 'e':
                os.system('cls')
                print(Fore.BLUE + "ASSIGNMENT OPERATORS" + Style.RESET_ALL)
                time.sleep(0.1)
                print('''Assignment operators are used to assign values to variables.
They include operators like =, +=, -=, *=, /=, and more.
Here are some examples:\n''')
                time.sleep(0.1)
                print("x = 5")
                time.sleep(0.1)
                print("x += 3 # Equivalent to x = x + 3")
                time.sleep(0.1)
                print("print(x) # Output: 8\n")
                time.sleep(0.1)
                print("x -= 2 # Equivalent to x = x - 2")
                time.sleep(0.1)
                print("print(x) # Output: 6\n")
                time.sleep(0.1)
                print("x *= 2 # Equivalent to x = x * 2")
                time.sleep(0.1)
                print("print(x) # Output: 12\n")
                time.sleep(0.1)
                print("x /= 3 # Equivalent to x = x / 3")
                time.sleep(0.1)
                print("print(x) # Output: 4.0\n")
                time.sleep(0.1)

                ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
                time.sleep(0.1)
                os.system('cls')

            elif sel == 'r':
                os.system('cls')
                return

# Loops
def OO7():
    while True:
        os.system('cls')
        data = (Fore.GREEN + "Loops" + Style.RESET_ALL)
        print(f'[]==================[]{data}[]==================[]')
        print("\tA - For Loop")
        time.sleep(0.1)
        print("\tB - Nested Loop")
        time.sleep(0.1)
        print("\tC - While Loop")
        time.sleep(0.1)
        print('[]================================================[]')

        sel = (input("Select A - C slides or R to return to menu ----> ")).lower()
        time.sleep(0.1)

        if sel == 'a':
            os.system('cls')
            print('''A for loop in Python is used to iterate over
a sequence (like a list, tuple, dictionary, set, or 
string) and execute a block of code for each item in 
the sequence.''')
            time.sleep(0.1)
            print('anime_suge = ["One punch man", "Bleach", "Solo leveling"]')
            time.sleep(0.1)
            print("for anime in anime_suge:")
            time.sleep(0.1)
            print(" print(anime)\n")
            time.sleep(0.1)
            print("Output:\n")
            time.sleep(0.1)
            print("One punch man")
            time.sleep(0.1)
            print("Bleach")
            time.sleep(0.1)
            print("Solo leveling")
            time.sleep(0.1)

            print("\nUsing range()")
            time.sleep(0.1)
            print('''The range() function generates a sequence of numbers,
which is useful for iterating a specific number of times.
\nFor example:\n''')
            time.sleep(0.1)
            print("for i in range(4):")
            time.sleep(0.1)
            print(" print(i)\n")
            time.sleep(0.1)
            print("Output:\n")
            time.sleep(0.1)
            print("0")
            time.sleep(0.1)
            print("1")
            time.sleep(0.1)
            print("2")
            time.sleep(0.1)
            print("3\n")
            time.sleep(0.1)

            ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        if sel == 'b':
            os.system('cls')
            print('''You can use nested loops to iterate over multiple sequences.
 Here some smaple for far more deeper understanding.\n''')
            time.sleep(0.1)
            print("while True:")
            time.sleep(0.1)
            print('anime_suge = ["solo leveling", "Bleach"]')
            time.sleep(0.1)
            print('anime = ["One punch man", "Naruto"]')
            time.sleep(0.1)
            print("for i in anime_suge:")
            time.sleep(0.1)
            print("  for a in anime:")
            time.sleep(0.1)
            print('    print(i, a)\n')
            time.sleep(0.1)
            print("Ouput:\n")
            time.sleep(0.1)
            print("solo leveling One punch man")
            time.sleep(0.1)
            print("solo leveling Naruto")
            time.sleep(0.1)
            print("Bleach One punch man")
            time.sleep(0.1)
            print("Bleach Naruto\n")
            time.sleep(0.1)

            ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        if sel == 'c':
            os.system('cls')
            print('''In Python, the while loop is a control flow statement
that allows code to be executed repeatedly based on a given
Boolean condition. The loop continues to execute as long as
the condition remains true. This type of loop is particularly
useful for scenarios where the number of iterations is not known
beforehand, making it an example of indefinite iteration.''')
            time.sleep(0.1)
            print("The basic syntax of a while loop in Python is as follows:\n")
            time.sleep(0.1)
            print("jun = True\n")
            time.sleep(0.1)
            print("while jun:")
            time.sleep(0.1)
            print('    moon = input("DO you like moon shinning at night (yes/no)")')
            time.sleep(0.1)
            print("    if moon =='yes':")
            time.sleep(0.1)
            print("        print('Moon keep shinning!!!!!')")
            time.sleep(0.1)
            print("        continue")
            time.sleep(0.1)
            print("    else:")
            time.sleep(0.1)
            print("        print('MOoon is now getting darker')\n")
            time.sleep(0.1)
            print("        break")
            time.sleep(0.1)
            print("if yes the Output will be:\n")
            time.sleep(0.1)
            print("Moon keep shinning!!!!!'")
            time.sleep(0.1)

            ret = input(Fore.RED + "Press enter to return..." + Style.RESET_ALL)
            time.sleep(0.1)
            os.system('cls')

        elif sel == 'r':
            os.system('cls')
            return

# List
def OO8():
    while True:
        os.system('cls')
        print("Lists are used to store multiple items in a single variable.\n")
        time.sleep(0.1)
        print("Key Characteristics:")
        time.sleep(0.1)
        print("Ordered: Items maintain their position.")
        time.sleep(0.1)
        print("Mutable: You can change, add, or remove elements.")
        time.sleep(0.1)
        print("Dynamic: Lists can grow or shrink during runtime.")
        time.sleep(0.1)
        print("Indexed: Each item has a position starting from 0.")
        time.sleep(0.1)         
        print("Common List Operations\n")
        time.sleep(0.1)
        print("Operation\t|Syntax\t\t\t\t|Description")
        time.sleep(0.1)
        print("Append\t\t|list.append(item)\t\t|Adds an item to the end")
        time.sleep(0.1)
        print("Insert\t\t|list.insert(index, item)\t|Inserts item at specified index")
        time.sleep(0.1)
        print("Remove\t\t|list.remove(item)\t\t|Removes first occurrence of item")
        time.sleep(0.1)
        print("Pop\t\t|list.pop(index)\t\t|Removes and returns item at index")
        time.sleep(0.1)
        print("Length\t\t|len(list)\t\t\t|Returns number of elements")
        time.sleep(0.1)
        print("Sort\t\tlist.sort()\t\t\t|Sorts the list (ascending by default)")
        time.sleep(0.1)
        print("Reverse\t\t|list.reverse()\t\t\t|Reverses the list order")
        time.sleep(0.1)

        print("Exampel of Common list operation")
        time.sleep(0.1)

        print('subset_name  = "jp"')
        time.sleep(0.1)
        print('subset_name1 = "take"\n')
        time.sleep(0.1)

        print('cool_user = ["jp", "denver", "take", "the goat", "meat" ]\n')
        time.sleep(0.1)

        print('print(cool_user)')
        time.sleep(0.1)
        print('print(cool_user[3])\n')
        time.sleep(0.1)

        print('cool_user.append("jp')
        time.sleep(0.1)
        print('print(cool_user)\n')
        time.sleep(0.1)

        print('cool_user.insert(3,"jp")')
        time.sleep(0.1)
        print('print(cool_user)\n')
        time.sleep(0.1)

        print('cool_user.pop()')
        time.sleep(0.1)
        print('print(cool_user)\n')
        time.sleep(0.1)

        print('print(len(cool_user))\n')
        time.sleep(0.1)

        print('cool_user.sort()')
        time.sleep(0.1)
        print('print(cool_user)\n')
        time.sleep(0.1)
        
        print('cool_user.reverse()')
        time.sleep(0.1)
        print('print(cool_user)\n')
        time.sleep(0.1)
        
        ret = input(Fore.RED + "Enter to return R..." + Style.RESET_ALL)
        time.sleep(0.1)
        os.system('cls')
        return



    
       