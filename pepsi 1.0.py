import time

while True:
    print ('------------------------')
    pepsi = int(input("How many cans of Pepsi? "))
    time.sleep(1)
    print(' ')
    if pepsi == 1488:
        time.sleep(1.5)
        print ("посхолочко")
        time.sleep(0.1)
        print(' ')
        time.sleep(1.5)
        print('ВКЛЮЧАЕМ ВЕНТИЛЯТОРЫ')
    elif pepsi >= 6:
        time.sleep(1.5)
        print('thats a lot')
        print(' ')
    elif pepsi <= 4:
        time.sleep(1.5)
        print ('this not enough')
        print (' ')
    else:
        time.sleep(1.5)
        print('good job')
        time.sleep(0.1)
        print(" ")
        time.sleep(1.5)
        print('bye')
        time.sleep(1)
        break
