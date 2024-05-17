# PyShell v1.0.1-alpha
# Developed by Nathan Gonzalez / LanPort
# Stockfish module required for chess capabilities.
print("Importing time module...")
import time
chessprompt = input("Do you have the stockfish module installed [y/n/s]?")
if chessprompt == "y":
    print("Intializing Stockfish...")
    from stockfish import Stockfish #type: ignore
elif chessprompt == "n":
    print("Go to https://pypi.org/project/stockfish/ to install stockfish.")
    input("Press enter to continue startup..")
elif chessprompt == "s":
    print("You have skipped stockfish initialization.")
else:
    print("Invalid input; starting without chess capabilities.")
    time.sleep(1)
print("Importing run functionality...")
from subprocess import call
print("Importing RNG...")
import random
print("Importing OS commands...")
import os
print("Setting booleans...")
UsingProgram = True
calcsuccess = False
UsingTermEmu = True
print("Importing math module...")
import math
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome!")
print("Please type commands in lowercase; commands are case sensitive.")
print("Command arguments have NOT been developed yet; this is just a fun little prototype :3")
print("gTTS MUST be installed via pip.")
while UsingProgram == True:    
    cmd = input("pyshell >")
    if cmd == "help":
        print("Current command list:")
        print("'clear': Clear the commandline.")
        print("'calc': Basic calculator.")
        print("'explorer': Open Windows Explorer (Windows Only.)")
        print("'quit': End current pyshell session.")
        print("'rolld20': Generates random number from 1-20. (Like a 20 side die!)")
        print("'game': RNG based minigame.")
        print("'run': Run a program. (OS Terminal Emulator reccomended for non-windows users.) ") # I have no idea if this is crossplatform or not... (Note)
        print("'pdb': Enter the python debugger environment. (RECCOMENDED ONLY FOR DEVELOPERS)")
        print("'os': Opens a OS terminal emulator")
    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "calc": # this originally just opened the calculator but i decided to build a full calculator (with bugs and everything!)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("------CALCULATOR------")
        print("What type of equation do you want to make?")
        print("1. Addition")
        print("2. Multiplication")
        print("3. Subtraction")
        print("4. Division")
        eqtype = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        x = input("1st number (X): ")
        y = input("2nd number (Y): ")
        x = int(x)
        y = int(y)
        if eqtype == "1":
            calcres = x + y
            print(calcres)
            calcsuccess = True
        elif eqtype == "2":
            calcres = x * y
            print(calcres)
            calcsuccess = True
        elif eqtype == "3":
            calcres = x - y
            print(calcres)
            calcsuccess = True
        elif eqtype == "4":
            if x == 0:
                print("NO.")
                x = 1
            elif y == 0:
                print("NO.")
                y = 1
            calcres = x / y
            print(calcres)
            calcsuccess = True
        else:
            print("Oops! Something went wrong.")
        if calcsuccess == True:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
    elif cmd == "explorer":
        call(["explorer.exe"])
    elif cmd == "hello": # tiny little easteregg :)
        print("Hello!")
    elif cmd == "rolld20": # might actually make like a full on dnd companion thing but this is mainly for RNG testing :P
        roll = random.randint(1, 20)
        print("You rolled a ",roll,".")
    elif cmd == "game": # 99% OF GAMBLERS QUIT RIGHT BEFORE THEY WIN!!!
        print("Let me explain the rules:")
        print("You pick a number and i pick a number.")
        print("If our numbers match you win!")
        print("If the numbers do NOT match i win!")
        print("Got that? OK!")
        print("Now we select a difficulty from Easy to Impossible.")
        print("Easy: Number 1-2 (1)")
        print("Normal: 1-6 (2)")
        print("Hard 1-20 (3)")
        print("Very Hard: 1-100 (4)")
        print("Impossible: 1-1000 (5)")
        diff = 0
        diff = input("Choose a difficulty (1-5): ")
        diff = int(diff)
        print(diff)
        if diff == 1:
            urnumber = input("Pick a number 1-2: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 2):
                print("You win!")
            else:
                print("You lost...")
        elif diff == 2:
            urnumber = input("Pick a number 1-6: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 6):
                print("You win!")
            else:
                print("You lose...")
        elif diff == 3:
            urnumber = input("Pick a number 1-20: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 20):
                print("You win!")
            else:
                print("You lose...")
        elif diff == 4:
            urnumber = input("Pick a number 1-100: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 100):
                print("Cool! You win!")
            else:
                print("You lost :(")
        elif diff == 5:
            urnumber = input("Pick a number 1-1000: ")
            urnumber = int(urnumber)
            if urnumber == random.randint(1, 1000):
                print("The RNGods have blessed you today lol (also you win btw :3)")
            else:
                print("I told you it was impossible...")
                print("also you lost rip bozo :)")
        else:
            print("Oops! Something went wrong.")        
            time.sleep(5)
    elif cmd == "quit":
        UsingProgram = False
    elif cmd == "os":
        print("OS Terminal Emulator")
        print("Use 'quittermemu' to exit the terminal.")
        while UsingTermEmu == True:
            oscom = input("terminal-$")
            if oscom == "quittermemu":
                UsingTermEmu = False
            else:
                os.system(oscom)
    elif cmd == "pdb":
        print("Use 'continue' to exit the Python debug environment.")
        breakpoint()
    else:
        print("Invalid Command. Commands MUST be lowercase. Use the 'help' command to view available commands.")
print("Thank you for using pyshell; See you next time!")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')