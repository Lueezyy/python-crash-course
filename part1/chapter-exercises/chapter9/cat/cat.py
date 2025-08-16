class Cat:
    '''An attempt to model a cat'''

    def __init__(self, name, age):
        '''Initialize name and age'''
        self.name = name
        self.age = age

    def nap(self):
        '''Simulate a cat napping'''
        print(f'{self.name} is now napping. Zzzz...')

    def eat(self):
        '''Simulate a cat eating'''
        print(f'{self.name} is now eating. Yum!')