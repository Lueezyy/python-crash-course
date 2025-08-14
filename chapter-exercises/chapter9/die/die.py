import random as r

class Die:
    '''An attempt to model a die'''
    def __init__(self, sides=6):
        '''Initialize the number of sides'''
        self.sides = sides
    
    def roll_die(self):
        '''An attempt to model rolling the die'''
        roll = r.randint(1, self.sides)
        print(f'You rolled a {roll}.')
