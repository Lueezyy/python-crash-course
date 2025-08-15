from pathlib import Path

path = Path('text_files/written.txt')

contents = 'I like programming.\n'
contents += "I can't wait to learn data analysis.\n"
contents += "Then, I'll be able to learn machine learning.\n"

path.write_text(contents)