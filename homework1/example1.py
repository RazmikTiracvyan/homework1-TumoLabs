numbers = []

while True:
    choose = int(input('choose 1 or 2: '))
    if choose != 1 and choose != 2:
        print('try again, choose 1 or 2')
        continue 
    elif choose == 1:
        x = int(input('say a number: '))
        numbers.append(x)
    else:
        break

print(sum(numbers))