while True:
    number = int(input('say a number: '))
    if number == 0:
        break
    elif number % 2 == 0:
        print('even number')
    else:
        print('odd number')
