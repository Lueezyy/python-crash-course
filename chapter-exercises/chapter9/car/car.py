'''A class used to represent gas cars'''
class Car:
    '''An attempt to represent a car'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def descriptive_name(self):
        '''Return a descriptive name'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print(f'This car has {self.odometer} miles.')

    def update_odometer(self, mileage):
        '''Set the odometer to the given value, 
        reject the change if it attempts to roll odometer back'''
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You cannot roll back the odometer.')
    
    def add_miles(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer += miles
        
    def fill_gas_tank(self):
        '''Print a statement that the gas is filled'''
        print("The car's gas tank is now full.")