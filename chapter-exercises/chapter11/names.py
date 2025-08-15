from formatname import get_formatted_name

print("Enter 'Q' at any time to quit.")
while True:
    first = input('\nEnter your first name: ')
    if first == 'q':
        break
    last = input('Enter your last name: ')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}.")