from colorama import Fore, Style
import time
import os
from Body_finals import OO2
OO2()

while True:
    os.system('cls')
    O2 = ("====PYTHON====")
    time.sleep(0.1)
    print(Fore.BLUE + O2 + Style.RESET_ALL)

    print("A - Print Statement ")
    time.sleep(0.1)
    print("B - Variables ")
    time.sleep(0.1)
    print("C - Data Types ")
    time.sleep(0.1)
    print("D - Operators ")
    time.sleep(0.1)
    print("E - Loops ")
    time.sleep(0.1)
    print("F - Lists ")
    time.sleep(0.1)
    print("G - End the program ")
    time.sleep(0.1)
    
     
    CHOICE = input("SELECT A LESSON YOU WANT TO LEARN IN PYTON ABOVE ---> ").lower().strip()

    if CHOICE == 'a':
        from Body_finals import OO3
        os.system('cls')
        OO3()
        
    elif CHOICE == 'b':
        from Body_finals import OO4
        os.system('cls')
        OO4()

    elif CHOICE == 'c':
        from Body_finals import OO5
        os.system('cls')
        OO5()
    
    elif CHOICE == 'd':
        from Body_finals import OO6
        os.system('cls')
        OO6()
    
    elif CHOICE == 'e':
        from Body_finals import OO7
        os.system('cls')
        OO7()

    elif CHOICE == 'f':
        from Body_finals import OO8
        os.system('cls')
        OO8()
          
    elif CHOICE == 'g':
        print(f"Program ended, thnaks for learning python")
        break
