changelog = """
  5.5 reborn change log:
  Removed garbage from the code (a ton of variables)
  -------------------------------
  5.1 reborn change log:
  add my telegram
  bug fix
  -------------------------------
  5.0 reborn change log:
  add difficulty selection
  add easter egg (???)
  author's words: не добавил
  -------------------------------
  4.0 reborn change log:
  add record
  add new credit of game, his name is Gabriel
  -------------------------------
  3.5 reborn change log:
  add my GitHub in menu
  add exit in menu
  -------------------------------
  3.0 reborn change log:
  add main menu
  -------------------------------
  2.5 reborn change log:
  add variables in code
   ------------------------------
  2.0 change log:
  add random
  add answer in code
  add guess in code"""
# -----------------------------------------
play = """
----menu----
play    
change log 
my GitHub  
my telegram
credits   
exit    
???  
"""
# ----------------------------------------- mode for record's
v1 = "your first record"
v2 = "you beat the record"
v3 = "you beat your own record"
v4 = "no records yet"
v5 = "best: "
v6 = "time: "
v7 = "----------"
v8 = "name of record?"
# ----------------------------------------- uhhhh, 1 to 1****
t1 = "number to number? (like 10, 100, 1000, 10000): "
import random
import time
import os

print('hello, its pepsi_5.5_reborn!')
print("""
        _________
     .-'         '-.
   .|               |.
   |                 |
   |      #####      |
   |    #########    |
   |   ###########   |
   |   ###     ###   |
   |   ###     ###   |
   |    #########    |
   |      #####      |
   |                 |
   |      pepsi      |
   |                 |
   |                 |
   '-._____________.-'
""")
print('--------------------------------')

while True:
    print(play)
    answer = input('choose: ')
    print("")
    
    if answer == "play":
        print("")
        answer = input(t1)
        if answer == "10":
            number = random.randint(1, 10)
        elif answer == "100":
            number = random.randint(1, 100)
        elif answer == "1000":
            number = random.randint(1, 1000)
        elif answer == "10000":
            number = random.randint(1, 10000)
                
        start_time = time.time()
        while True:
            guess = int(input('number?: '))
            if guess < number:
                print("nah, that's not enough")
            elif guess > number:
                print("nah, that's a lot")
            else:
                print(f'yeah, you win, correct number {number}')
                end_time = time.time()
                ft = round(end_time - start_time, 2)

                if os.path.exists("leaderboard.txt"):
                    f = open("leaderboard.txt", "r")
                    data = f.read().split(",")
                    bn = data[0]
                    bt = float(data[1])
                    f.close()
                else:
                    bt = float('inf')
                    bn = "none"

                if ft < bt:
                    if bn == "none":
                        print(v1)
                        bn = input(v8)
                    else:
                        tn = input(v8)
                        if tn == bn:
                            print(v3)
                        else:
                            print(v2)
                        bn = tn
                    bt = ft
                    f = open("leaderboard.txt", "w")
                    f.write(bn + "," + str(bt))
                    f.close()

                print(v7)
                if bn == "none":
                    print(v4)
                else:
                    print(v5 + bn)
                    print(v6 + str(bt) + "s")
                print(v7)

                time.sleep(1)
                print('see you in next game!')
                time.sleep(1.5)
                break
                
    if answer == "change log":
        print(changelog)
    elif answer == "my GitHub":
        print("https://github.com/mishkagumiberr-star")
    elif answer == "my telegram":
        print("t.me/peshera_treta")
    elif answer == "credits":
        print("game by tret_game")
        print("co-creator Gabriel")
    elif answer == "exit":
        print("bye")
        break
    elif answer == "???":
        while True:
               print("--------------------------")
               time.sleep(0.1)
               print("PEPSI FOREVER")
               time.sleep(0.1)
