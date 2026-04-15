# pepsi 3.0 reborn change log = r-j
r = ("3.0 reborn change log:")
j = ("add main menu (new)")
# pepsi 2.5 reborn change log = d-f
d = ("2.5 reborn change log:")
f = ("add variables in code")
# pepsi 2.0 change log (old) = e-p
e = ("2.0 change log:")
o = ("add random")
i = ("add answer in code")
p = ("add guess in code")
# ----------------------------------------- game menu q-z
q = ("    play    ")
w = (" change log ")
z = ("   credit   ")
import random
import time

print('hello, its pepsi_3.0_reborn!')
print('--------------------------------')

while True:
    print("")
    print("----menu----")
    print(q)
    print(w)
    print(z)
    answer = input('choose: ')
    if answer == "play":
        print("")
        print('goodluck!')
        print('--------------------------------')
        number = random.randint(1, 100)
        while True:
            guess = int(input('number? (1-100): '))
            if guess < number:
                print("nah, that's not enough")
            elif guess > number:
                print("nah, that's a lot")
            else:
                print(f'yeah, you win, correct number {number}')
                time.sleep(1)
                print('see you in next game!')
                time.sleep(1.5)
                break           
    elif answer == "change log":
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
    elif answer == "credit":
        print("game by tret_game")
