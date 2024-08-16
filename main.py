import keyboard
import time
import os

banner = """
_   __           _   _            
| | / /          | | | |           
| |/ /  ___ _   _| |_| | __ ___  __
|    \\ / _ \\ | | |  _  |/ _` \\ \\/ /
| |\\  \\  __/ |_| | | | | (_| |>  < 
\\_| \\_/\\___|\\__, \\_| |_|\\__,_/_/\\_\\
             __/ |                 
            |___/ 
1.0                 
"""
print(banner)

running = True
if not os.path.exists('macros'):
    os.makedirs('macros')

while running:
    print("1. repeat key clicks for N times (Key clicks begin after 3 seconds)")
    print("2. write a macro")
    print("3. run a macro (Key clicks begin after 3 seconds)")
    print("4. view macros")
    print("5. Autoclick")
    print("6. exit")
    choice = input(">>> ")
    if choice == "1":
        print("Enter key to repeat:")
        key = input(">>> ")
        print("Enter number of times to repeat:")
        n = input(">>> ")
        if not n.isdigit():
            print("Please enter a valid number.")
            continue
        time.sleep(3)
        for i in range(int(n)):
            keyboard.press_and_release(key)
            time.sleep(0.1)
    elif choice == "2":
        print("Enter macro name:")
        macro_name = input(">>> ")
        print("Macro steps (Type it in):")
        macro = input(">>> ")
        with open(f"macros/{macro_name}.txt", "w") as f:
            f.write(macro)
            print(f"Macro file written in macros/{macro_name}.txt")
    elif choice == "3":
        print("Enter macro name (e.g. Macro.txt):")
        macro_to_run = input(">>> ")
        try:
            with open(f"macros/{macro_to_run}", "r") as f:
                time.sleep(3)
                keyboard.write(f.read())
        except FileNotFoundError:
            print("Macro file not found")
    elif choice == "4":
        print("Current macros available:")
        for file in os.listdir('macros'):
            if file.endswith(".txt"):
                print(file)
    elif choice == "5":
        print("Not available yet!")
    elif choice == "6":
        running = False
    else:
        print("Invalid choice, please select 1-4.")
