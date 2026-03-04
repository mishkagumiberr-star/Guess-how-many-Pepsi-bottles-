import time
import random

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

while True:
    secret_pepsi = random.randint(1, 200)
    attempts = 0
    current_color = "" 

    print(f"{CYAN}=== NEW GAME STARTED ==={RESET}")
   
    
    while True:
        try:
            pepsi = int(input(f"{current_color}how many pepsi? {RESET}"))
            attempts += 1
            
            print(f"{current_color}------------------------------------------------------{RESET}")
            
            if pepsi == 228:
                print('\a')
                current_color = RED 
                time.sleep(1)
                print(f"{RED}ЧИТ КОД 228: СИСТЕМА ОКРАШЕНА{RESET}")
                time.sleep(0.5)
                print(f"{RED}РЕЖИМ КРАСНОГО ТЕКСТА ON{RESET}")

            elif pepsi == 1488:
                print('\a')
                current_color = RED 
                time.sleep(1)
                print(f"{RED}ПОСХАЛОЧКО! ВЕНТИЛЯТОРЫ!{RESET}")
                time.sleep(0.5)
                print(f"{RED}ЧИТ КОД 1488: ПОЛНЫЙ ПЕРЕГРЕВ{RESET}")

            elif pepsi > secret_pepsi:
                time.sleep(1)
                print(f"{current_color}this so many, attempts {attempts}{RESET}")

            elif pepsi < secret_pepsi:
                time.sleep(1)
                print(f"{current_color}this not enough, attempts {attempts}{RESET}")

            else:
                
                print('\a')
                time.sleep(1.5)
                print(f"{GREEN}good job vro! It was {secret_pepsi}{RESET}")
                print(f"{GREEN}total attempts is {attempts}{RESET}")
                break 
                
        except ValueError:
            print(f"{RED}ERROR: Вводи только числа!{RESET}")

    
    print(" ")
    choice = input(f"{CYAN}Play again? (y/n): {RESET}").lower()
    
    if choice != 'y':
        print(f"{YELLOW}Shutting down... Bye!{RESET}")
        time.sleep(1.5)
        break 
