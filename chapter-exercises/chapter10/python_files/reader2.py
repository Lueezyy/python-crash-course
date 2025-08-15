from pathlib import Path

try:
    path = Path('text_files/cats.txt')
    contents = path.read_text()
except FileNotFoundError:
    print(f"Could not find '{path}'.")
else:
    print(contents)