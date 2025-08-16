from pathlib import Path
import json

def write():
    numbers = [3, 14, 15, 92, 653, 5897]
    path = Path('json_files/numbers.json')
    contents = json.dumps(numbers)
    path.write_text(contents)

def read():
    path = Path('json_files/numbers.json')
    contents = path.read_text()
    numbers = json.loads(contents)
    print(numbers)
