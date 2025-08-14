from classical import class_set

print(class_set('antonio vivaldi', 'the four seasons', 12))
print(class_set('johann sebastian bach', 'the brandenburg concertos', 19))
print(class_set('johann sebastian bach', 'the well-tempered clavier'))

while True:
    choice = input('Add a musical set? (y/n): ').strip().lower()
    if choice == 'n':
        break
    name = input('Who is the composer? ')
    title = input('What is the name of the set? ')
    print(class_set(name, title))