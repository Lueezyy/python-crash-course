from pathlib import Path
import json

def get_fav(path):
    if path.exists():
        contents = path.read_text()
        fav_num = json.loads(contents)
        return fav_num
    else:
        return None

def set_fav(path):
    while True:
        try:
            fav_num = int(input('What is your favorite number? '))
            break
        except:
            print('Please enter an integer.')
    contents = json.dumps(fav_num)
    path.write_text(contents)
    return fav_num

def tell_fav():
    path = Path('json_files/fav_num.json')
    fav_num = get_fav(path)
    if fav_num:
        print(f'Your favorite number is {fav_num}.')
    else:
        fav_num = set_fav(path)
        print("I'll remember your favorite number for next time.")

tell_fav()