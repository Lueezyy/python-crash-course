from pathlib import Path

def the(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'File {path} not found.')
    else:
        print(f"This file says 'the' {contents.lower().count('the ')} times.")

filenames = ['alice.txt', 
    'frankenstein.txt',
    'jane_eyre.txt',
    'pride_and_prejudice.txt']
for filename in filenames:
    path = Path(f'text_files/{filename}')
    the(path)