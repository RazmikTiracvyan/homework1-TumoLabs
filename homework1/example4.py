import random

randomNumber = random.randint(1, 10)

while True:
    guess = int(input('guess a number [1, 10] : '))
    if randomNumber == guess:
        print('you are right')
        break
    elif randomNumber > guess:
        print('your number is smaller try bigger number')
        continue
    else :
        print('your number is bigger try smaller number')
        continue