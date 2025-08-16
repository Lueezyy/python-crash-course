while True:
    print('\nGive two numbers to add together.')
    print('Press Q to quit.')
    try:
        first = input('What is the first number: ')
        if first.lower() == 'q':
            break
        else:
            first = int(first)
        second = input('What is the second number: ')
        if second.lower() == 'q':
            break
        else:
            second = int(second)
    except ValueError:
        print('Give integer values.')
    else:
        print(f'The answer is {first + second}.')