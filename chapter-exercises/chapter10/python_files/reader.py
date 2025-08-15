from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.strip()


print(f'{pi_string[:52]}...')
print(len(pi_string))

birthday = input('Enter your birthday in form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi.')
else:
    print('Your birthday does not appear in the first million digits of pi.')