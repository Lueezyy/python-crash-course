from pathlib import Path

path = Path('text_files/guest.txt')

full_contents = ''
while True:
    contents = input('What is your name? (Q to cancel): ')
    if contents.lower() == 'q':
        break
    else:
        full_contents += f'{contents}\n'

path.write_text(full_contents)