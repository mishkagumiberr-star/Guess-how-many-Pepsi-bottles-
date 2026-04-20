# pepsi 5.0 reborn change log = a1-a4
a1 = ("5.0 reborn change log:")
a2 = ("add difficulty selection")
a3 = ("add easter egg (???)")
a4 = ("author's words: в следущем обновлении будет русский перевод, зуб даю (нет)")
# pepsi 4.0 reborn change log = q1-q3
q1 = ("4.0 reborn change log:")
q2 = ("add record")
q3 = ("add new credit of game, his name is Gabriel")
# pepsi 3.5 reborn change log = c-x
c = ("3.5 reborn change log:")
s = ("add my GitHub in menu")
x = ("add exit in menu")
# pepsi 3.0 reborn change log = r-j
r = ("3.0 reborn change log:")
j = ("add main menu")
# pepsi 2.5 reborn change log = d-f
d = ("2.5 reborn change log:")
f = ("add variables in code")
# pepsi 2.0 change log (old) = e-p
e = ("2.0 change log:")
o = ("add random")
i = ("add answer in code")
p = ("add guess in code")
# ----------------------------------------- game menu q-g
q = ("    play    ")
w = (" change log ")
h = (" my GitHub  ")
z = ("  credits   ")
g = ("    exit    ")
u = ("    ???     ")
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

print('hello, its pepsi_.0_reborn!')
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
    print("")
    print("----menu----")
    print(q)
    print(w)
    print(h)
    print(z)
    print(g)
    print(u)
    answer = input('choose: ')
    
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
                
    elif answer == "change log":
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print("")
        print(q1)
        print(q2)
        print(q3)
        print("")
        print(c)
        print(s)
        print(x)
        print("")
        print(r)
        print(j)
        print("")
        print(d)
        print(f)
        print("")
        print(e)
        print(o)
        print(i)
        print(p)
    elif answer == "my GitHub":
        print("https://github.com/mishkagumiberr-star")
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