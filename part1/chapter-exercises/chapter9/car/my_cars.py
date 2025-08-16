from car import Car
from electric_car import ElectricCar as EC

my_lambo = Car('lamborghini', 'temerario', 2026)
print(my_lambo.descriptive_name())

my_rivac = EC('rivac', 'nevera r', 2025)
my_rivac.battery.battery_size = 108
print(my_rivac.descriptive_name())