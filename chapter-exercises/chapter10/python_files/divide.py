print('Give me two numbers to divide.')
print('Enter Q to quit.')

while True:
    first = input('\nFIrst number: ')
    if first.lower() == 'q':
        break
    second = input('Second number: ')
    if second.lower() == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print('Undefined')
    else:
        print(answer)