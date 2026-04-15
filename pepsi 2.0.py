import random
import time

print('hello, this is pepsi 2.0!')
print('--------------------------------')
time.sleep(0.5)

answer = input('want see change log? yes/no ')
if answer == "yes":
    print('change log:')
    time.sleep(1)
    print('add random (new)')
    time.sleep(1)
    print('add answer in code (new)')
    time.sleep(1)
    print('add guess to code (new)')
time.sleep(1)
print('--------------------------------')    
answer = input ('want to play the game? yes/no ')
if answer == "yes":
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