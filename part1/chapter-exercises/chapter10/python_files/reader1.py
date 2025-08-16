from pathlib import Path

path = Path('text_files/english.txt')
contents = path.read_text()

message = ''
for line in contents.splitlines():
    message += f'{line.strip()} '
    
print(message)
message = message.replace('English', 'Spanish')
print(message)