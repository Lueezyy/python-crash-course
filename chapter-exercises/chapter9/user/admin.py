from user import User

class Privileges:
    def __init__(self, privileges=['can delete post', 'can ban user']):
        self.privileges = privileges

    def show_priveleges(self):
        print(f'This user has the following privileges: {self.privileges}')

class Admin(User):
    def __init__(self, first, last, age, gender, major, status):
        super().__init__(first, last, age, gender, major, status)
        self.privileges = Privileges()