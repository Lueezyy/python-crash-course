class User:
    def __init__(self, first, last, age, gender, major, status):
        self.first = first.title()
        self.last = last.title()
        self.age = age
        self.gender = gender
        self.major = major
        self.status = status
        self.login_attempts = 0

    def describe_user(self):
        if self.status == 'alive':
            print(f'\n{self.first} {self.last} is a {self.age} '
            f'year old {self.gender} who studies {self.major}.')
        elif self.status == 'dead':
            print(f'\n{self.first} {self.last} died at {self.age} '
            f'years old and was a {self.gender} who studied {self.major}.')
    
    def greet_user(self):
        print(f'\nHello {self.first} {self.last}.')

    def inc_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
