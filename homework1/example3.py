operations = ['+', '-', '/', '*']
n1 = int(input('Choose first number: '))

print("Available operations:", operations)
oper = input('Choose operator from the list: ')

n2 = int(input('Choose second number: '))

if oper == '+':
    result = n1 + n2
elif oper == '-':
    result = n1 - n2
elif oper == '/':
    result = n1 / n2
elif oper == '*':
    result = n1 * n2
else:
    result = "Invalid operator"

print(f'The result of {n1} {oper} {n2} is: {result}')
