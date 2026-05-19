x = ("change log:")
# pepsi 2.5 reborn change log = d-f
d = ("2.5 reborn change log:")
f = ("add variables in code (new)")
# pepsi 2.0 change log (old) = e-p
e = ("2.0 change log:")
o = ("add random")
i = ("add answer in code")
p = ("add guess in code")
import random
import time

print('hello, its pepsi_2.5_reborn!')
print('--------------------------------')
answer = input ('want to see change log? yes/no ')
if answer == "yes":
    print(x)
    print("")
    print(d)
    print(f)
print("--------------------------------")
answer = input ('want to see 2.0 change log? yes/no ')
if answer == "yes":
    print(e)
    print("")
    print(o)
    print(i)
    print(p)
print("--------------------------------")
answer = input ('want to play the game? yes/no ')
if answer == "yes":
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
            print('bye!')
            time.sleep(1.5)
            break
