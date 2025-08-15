from pathlib import Path
import json

def get_name(path):
    '''Get stored username if available'''
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_info(infopath):
    if infopath.exists():
        contents = infopath.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_name(path):
    '''Prompt for a new username'''
    username = input('What is your name? ')
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def get_new_info(infopath):
    user_info = {}
    while True:
        try:
            age = int(input('How old are you? '))
        except:
            print('Enter a valid integer...')
        else:
            break
    user_info['age'] = age
    language = input('What language do you speak best? ')
    user_info['language'] = language.title()
    contents = json.dumps(user_info)
    infopath.write_text(contents)
    return user_info

def greet():
    '''Greet the user by name and info'''
    path = Path('json_files/username.json')
    infopath = Path('json_files/user_info.json')
    username = get_name(path)
    user_info = get_info(infopath)
    while True:
        if username:
            answer = input(f'Are you {username}? (y/n): ')
            if answer == 'y':
                print(f'Welcome back {username}.')
                if user_info:
                    print(f"What we know about you: {user_info}")
                    break
                else:
                    user_info = get_new_info(infopath)
                    print("We'll keep this info... just in case.")
                    break
            elif answer == 'n':
                username = get_new_name(path)
                user_info = get_new_info(infopath)
                print(f"We'll remember you when you come back {username}.")
                break
            else:
                print("Only respond with a 'y' or a 'n'.")
        
greet()