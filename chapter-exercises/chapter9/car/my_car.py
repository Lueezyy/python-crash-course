from car import Car

new_car = Car('mcLaren', '750S', 2025)
print(new_car.descriptive_name())

new_car.odometer = 25
new_car.read_odometer()