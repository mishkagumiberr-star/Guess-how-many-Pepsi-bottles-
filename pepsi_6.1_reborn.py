changelog = """
  6.1 rebotn change log:
  add webbrowser to code
  -------------------------------
  6.0 reborn change log:
  co-creator "Gabriel" has removed. Reason: send IP logger
  add match-case in code
  removed garbage from the code (if else)
  game kernel update to match-case
  -------------------------------
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
  add guess in code
  """
# -----------------------------------------
play = """
----menu----
play
change log
github
telegram
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

import time
import random
import os
import webbrowser

print('hello, its pepsi_6.1_reborn!')
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
    match answer:
        case "play":
            diff = input(t1)
            match diff:
                case "10":
                    number = random.randint(1, 10)
                case "100":
                    number = random.randint(1, 100)
                case "1000":
                    number = random.randint(1, 1000)
                case "10000":
                    number = random.randint(1, 10000)
                case _:
                    print("wrong number")
                    continue

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
        case "change log":
            print(changelog)
        case "github":
            webbrowser.open("https://github.com/mishkagumiberr-star")
        case "telegram":
            webbrowser.open("t.me/peshera_treta")
        case "credits":
            print("game created by tret_game")
        case "exit":
            break
        case "???":
            while True:
                print("--------------------------")
                time.sleep(0.1)
                print("PEPSI FOREVER")
                time.sleep(0.1)
