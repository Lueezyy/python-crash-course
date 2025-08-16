from car import Car

my_car = Car('koenigsegg', 'jesko absolut', 2025)
print(my_car.descriptive_name())

my_car.odometer = 20
my_car.read_odometer()
my_car.update_odometer(30)
my_car.read_odometer()

your_car = Car('toyota', 'highlander', 2020)
print(your_car.descriptive_name())

your_car.update_odometer(83_500)
your_car.read_odometer()

your_car.add_miles(183)
your_car.read_odometer()