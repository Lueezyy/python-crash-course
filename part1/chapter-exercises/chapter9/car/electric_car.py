'''A set of classes used to represent electric cars'''

from car import Car

class Battery:
    '''An attempt to model a battery for an electric car'''

    def __init__(self, battery_size=60):
        '''Initialize the battery's attributes'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print(f'This car has a {self.battery_size}-KWh battery.')

    def get_range(self):
        '''Print a statement about the range this battery provides'''
        if self.battery_size == 75:
            range = 330
        elif self.battery_size == 60:
            range = 279
        elif self.battery_size == 108:
            range = 250
        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size < 75:
            self.battery_size = 75
            print(f"This car's battery has been upgraded.")
        else:
            print(f"This car's battery is unable to upgrade.")

class ElectricCar(Car):
    '''An attempt to represent an electric car specifically'''

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class, 
        then initialize attributes specific to an electric car'''
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        '''Electric cars don't have gas tanks...'''
        print("You fool, this car doesn't have a gas tank.")